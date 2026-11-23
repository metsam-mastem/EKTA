#!/usr/bin/env python3
"""Validate EKTA concept metadata, taxonomy references, and local Markdown links."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from ekta_runtime.content import ContentError, load_yaml_file, split_front_matter  # noqa: E402

CONCEPT_DIR = ROOT / "encyclopedia" / "concepts"
SCHEMA_PATH = ROOT / "schemas" / "concept.schema.json"
REQUIRED_HEADING_GROUPS = (
    ("## Definition",),
    ("## Scope", "## Scope and disambiguation"),
    ("## Purpose", "## Purpose and role"),
    ("## Role", "## Purpose and role"),
    ("## Mechanism",),
    ("## Trade-offs",),
    ("## Verification",),
)


def validate() -> list[str]:
    errors: list[str] = []
    seen: dict[str, Path] = {}
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    schema_validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )

    domain_items = load_yaml_file(ROOT / "taxonomy" / "domains.yml").get("domains", [])
    layer_items = load_yaml_file(ROOT / "taxonomy" / "layers.yml").get("layers", [])
    territory_items = load_yaml_file(ROOT / "taxonomy" / "territories.yml").get("territories", [])
    taxonomy = {
        "domains": {item["id"] for item in domain_items if isinstance(item, dict) and "id" in item},
        "layers": {item["id"] for item in layer_items if isinstance(item, dict) and "id" in item},
        "knowledge_types": set(load_yaml_file(ROOT / "taxonomy" / "knowledge-types.yml").get("knowledge_types", [])),
    }

    if len(territory_items) != 26:
        errors.append(f"taxonomy/territories.yml: expected exactly 26 approved territories, found {len(territory_items)}")
    seen_territories: set[str] = set()
    for territory in territory_items:
        if not isinstance(territory, dict) or not territory.get("id"):
            errors.append("taxonomy/territories.yml: each territory must have a stable id")
            continue
        territory_id = territory["id"]
        if territory_id in seen_territories:
            errors.append(f"taxonomy/territories.yml: duplicate territory ID {territory_id}")
        seen_territories.add(territory_id)
        for domain_id in territory.get("domain_ids", []):
            if domain_id not in taxonomy["domains"]:
                errors.append(f"taxonomy/territories.yml: {territory_id} references unknown domain {domain_id}")

    for path in sorted(CONCEPT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        try:
            metadata, _body = split_front_matter(text)
        except ContentError as exc:
            errors.append(f"{relative}: {exc}")
            continue

        for problem in sorted(schema_validator.iter_errors(metadata), key=lambda e: list(e.path)):
            location = ".".join(str(part) for part in problem.path) or "front matter"
            errors.append(f"{relative}: schema error at {location}: {problem.message}")

        concept_id = metadata.get("id")
        if isinstance(concept_id, str):
            if concept_id in seen:
                errors.append(f"duplicate ID {concept_id}: {seen[concept_id]} and {path}")
            seen[concept_id] = path

        for field, known_values in taxonomy.items():
            for value in metadata.get(field, []) if isinstance(metadata.get(field, []), list) else []:
                if value not in known_values:
                    errors.append(f"{relative}: unknown {field} ID {value}")

        for alternatives in REQUIRED_HEADING_GROUPS:
            if not any(heading in text for heading in alternatives):
                errors.append(f"{relative}: missing one of {alternatives}")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0]
            target_path = (path.parent / relative).resolve()
            if relative and not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(f"ERROR: {problem}" for problem in problems))
        sys.exit(1)
    print("PASS: EKTA schema, taxonomy, documentation, and link checks passed")
