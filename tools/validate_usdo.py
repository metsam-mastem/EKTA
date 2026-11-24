#!/usr/bin/env python3
"""Validate the USDO facet registry, JSON Schema, and canonical examples."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "taxonomy" / "usdo-facets.yml"
SCHEMA = ROOT / "schemas" / "usdo-entity.schema.json"
EXAMPLES = [ROOT / "examples" / "USDO_CPU_EXAMPLE.yml"]


def validate() -> list[str]:
    errors: list[str] = []
    try:
        registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
    except (OSError, json.JSONDecodeError, yaml.YAMLError, jsonschema.SchemaError) as exc:
        return [f"Foundation load/schema error: {exc}"]

    facets = registry.get("facets", []) if isinstance(registry, dict) else []
    ids = [item.get("id") for item in facets if isinstance(item, dict)]
    expected = {"ontology", "dimension", "scope", "scale", "layer", "classification",
                "architecture", "topology", "circuit", "relation", "dynamics", "evaluation"}
    if len(ids) != 12:
        errors.append(f"Expected 12 USDO facets, found {len(ids)}")
    if len(ids) != len(set(ids)):
        errors.append("Duplicate facet identifiers in taxonomy/usdo-facets.yml")
    if set(ids) != expected:
        errors.append(f"Facet registry mismatch: expected {sorted(expected)}, found {sorted(ids)}")

    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    for path in EXAMPLES:
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: cannot load YAML: {exc}")
            continue
        for problem in validator.iter_errors(record):
            location = ".".join(str(part) for part in problem.path) or "record"
            errors.append(f"{path.relative_to(ROOT)}: schema error at {location}: {problem.message}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(f"ERROR: {problem}" for problem in problems))
        sys.exit(1)
    print("PASS: USDO facet registry, JSON Schema, and examples are valid")
