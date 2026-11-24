#!/usr/bin/env python3
"""Validate UPDS document records in the canonical repository."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "upds-document.schema.json"
RECORDS_DIR = ROOT / "upds" / "records"

sys.path.insert(0, str(ROOT / "tools"))
from upds_validation import validate_records  # noqa: E402


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    json_records = []
    source_paths = sorted(RECORDS_DIR.rglob("*.yml")) + sorted(RECORDS_DIR.rglob("*.yaml"))
    for path in source_paths:
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            print(f"ERROR: {path.relative_to(ROOT)}: invalid YAML: {exc}")
            return 1
        if not isinstance(record, dict):
            print(f"ERROR: {path.relative_to(ROOT)}: record must be a YAML mapping")
            return 1
        json_records.append(record)

    if not json_records:
        print("ERROR: no UPDS records found")
        return 1

    errors = validate_records(json_records, schema)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"PASS: validated {len(json_records)} UPDS document record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
