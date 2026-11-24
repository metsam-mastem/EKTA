from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "orchestration" / "WORKSTREAMS.yml"
SCHEMA = ROOT / "schemas" / "workstream-registry.schema.json"


def validate_registry(registry_path: Path = REGISTRY, schema_path: Path = SCHEMA) -> list[str]:
    try:
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError, json.JSONDecodeError) as exc:
        return [f"cannot load orchestration registry/schema: {exc}"]

    errors = [
        f"schema: {error.message} at {list(error.absolute_path)}"
        for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(registry)
    ]
    if errors:
        return errors

    streams = registry["workstreams"]
    allowed = set(registry["policy"]["status_vocabulary"])
    ids = [item["id"] for item in streams]
    prs = [item["pr"] for item in streams]
    branches = [item["branch"] for item in streams]

    for label, values in (("id", ids), ("PR", prs), ("branch", branches)):
        if len(values) != len(set(values)):
            errors.append(f"duplicate workstream {label}")

    known = set(ids)
    graph: dict[str, list[str]] = {}
    for item in streams:
        if item["status"] not in allowed:
            errors.append(f"{item['id']}: unknown status {item['status']}")
        graph[item["id"]] = []
        for dependency in item["dependencies"]:
            if dependency not in known:
                errors.append(f"{item['id']}: unknown dependency {dependency}")
            elif dependency == item["id"]:
                errors.append(f"{item['id']}: self-dependency")
            else:
                graph[item["id"]].append(dependency)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, trail: tuple[str, ...] = ()) -> None:
        if node in visiting:
            errors.append("dependency cycle: " + " -> ".join((*trail, node)))
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph.get(node, []):
            visit(dependency, (*trail, node))
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate EKTA parallel workstream registry")
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--schema", type=Path, default=SCHEMA)
    args = parser.parse_args()
    errors = validate_registry(args.registry, args.schema)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: EKTA workstream registry schema, IDs, PRs, branches, statuses, dependencies")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
