#!/usr/bin/env python3
"""Validation primitives for UPDS document records."""
from __future__ import annotations

from collections import Counter
from typing import Any, Iterable

import jsonschema


def validate_records(records: Iterable[dict[str, Any]], schema: dict[str, Any]) -> list[str]:
    """Validate records against the schema and detect duplicate stable identifiers."""
    errors: list[str] = []
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    materialized = list(records)
    ids: list[str] = []

    for index, record in enumerate(materialized):
        if not isinstance(record, dict):
            errors.append(f"record[{index}]: expected an object")
            continue
        for issue in sorted(validator.iter_errors(record), key=lambda err: list(err.path)):
            location = ".".join(str(part) for part in issue.path) or "record"
            errors.append(f"record[{index}] {location}: {issue.message}")
        record_id = record.get("id")
        if isinstance(record_id, str):
            ids.append(record_id)

    for record_id, count in Counter(ids).items():
        if count > 1:
            errors.append(f"duplicate document ID: {record_id} ({count} records)")
    return errors
