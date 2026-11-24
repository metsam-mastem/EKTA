#!/usr/bin/env python3
"""Validate VEL example files against JSON Schema and semantic rules."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

import jsonschema
from ekta_runtime.vel import load_model, validate_model

SCHEMA_PATH = ROOT / "schemas" / "vel-model.schema.json"


def validate(path: Path) -> list[str]:
    model = load_model(path)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = [
        f"SCHEMA {error.json_path}: {error.message}"
        for error in validator.iter_errors(model)
    ]
    errors.extend(
        f"{item['severity']} {item['code']} {item['path']}: {item['message']}"
        for item in validate_model(model)
    )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="VEL JSON files; defaults to projects/vel/examples/*.json")
    args = parser.parse_args()
    paths = args.paths or sorted((ROOT / "projects" / "vel" / "examples").glob("*.json"))
    failed = False
    for path in paths:
        try:
            errors = validate(path)
        except Exception as exc:
            errors = [f"LOAD_ERROR: {exc}"]
        if errors:
            failed = True
            print(f"FAIL: {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS: {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
