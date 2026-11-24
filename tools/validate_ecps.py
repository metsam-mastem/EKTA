#!/usr/bin/env python3
"""Validate ECPS projection manifests against JSON Schema and semantic contracts."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ECPS_ROOT = ROOT / "projects" / "ecps"
sys.path.insert(0, str(ECPS_ROOT / "src"))

import jsonschema
from ecps.contracts import validate_manifest

SCHEMA_PATH = ROOT / "schemas" / "ecps-projection.schema.json"
DEFAULT_EXAMPLES = ECPS_ROOT / "examples"


def validate(path: Path) -> list[str]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    findings = [f"SCHEMA {error.json_path}: {error.message}" for error in validator.iter_errors(manifest)]
    findings.extend(f"{item['severity']} {item['code']} {item['path']}: {item['message']}" for item in validate_manifest(manifest))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="ECPS projection manifest paths")
    args = parser.parse_args()
    paths = args.paths or sorted(DEFAULT_EXAMPLES.glob("*.json"))
    if not paths:
        print("BLOCKED: no ECPS projection manifests found")
        return 2
    failed = False
    for path in paths:
        try:
            findings = validate(path)
        except Exception as exc:
            findings = [f"LOAD_ERROR: {exc}"]
        if findings:
            failed = True
            print(f"FAIL: {path}")
            for finding in findings:
                print(f"  - {finding}")
        else:
            print(f"PASS: {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
