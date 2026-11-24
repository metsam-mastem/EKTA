#!/usr/bin/env python3
"""Validate the non-canonical engineering organization crosswalk."""
from __future__ import annotations

import json
import sys
import jsonschema
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "taxonomy" / "ENGINEERING_ORGANIZATION_VIEW.json"
TERRITORIES = ROOT / "taxonomy" / "territories.yml"


def validate() -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot load organization registry: {exc}"]

    try:
        schema_path = ROOT / "schemas" / "engineering-organization.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(data)
    except (OSError, json.JSONDecodeError, jsonschema.SchemaError, jsonschema.ValidationError) as exc:
        return [f"organization registry schema validation failed: {exc}"]

    try:
        import yaml
        territory_data = yaml.safe_load(TERRITORIES.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"cannot load canonical territory registry: {exc}"]

    known = {
        item.get("id")
        for item in territory_data.get("territories", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    areas = data.get("macro_areas")
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if data.get("status") not in {"DRAFT", "PROPOSED", "REVIEWED", "APPROVED"}:
        errors.append("status must be a recognized maturity state")
    policy = data.get("classification_policy", {})
    if policy.get("macro_view_role") != "crosswalk_only":
        errors.append("macro_view_role must remain crosswalk_only")
    if policy.get("no_new_territory_ids") is not True:
        errors.append("macro view must not create new territory IDs")
    if not isinstance(areas, list) or not areas:
        return errors + ["macro_areas must be a non-empty array"]

    seen: set[str] = set()
    for index, area in enumerate(areas):
        if not isinstance(area, dict):
            errors.append(f"macro_areas[{index}] must be an object")
            continue
        area_id = area.get("id")
        if not isinstance(area_id, str) or not area_id:
            errors.append(f"macro_areas[{index}] requires a non-empty id")
            continue
        if area_id in seen:
            errors.append(f"duplicate macro-area id: {area_id}")
        seen.add(area_id)
        if not area.get("label") or not area.get("persian"):
            errors.append(f"{area_id}: label and persian label are required")
        territory_ids = area.get("territory_ids")
        if not isinstance(territory_ids, list) or not territory_ids:
            errors.append(f"{area_id}: territory_ids must be a non-empty list")
            continue
        if len(territory_ids) != len(set(territory_ids)):
            errors.append(f"{area_id}: duplicate territory mapping")
        for territory_id in territory_ids:
            if territory_id not in known:
                errors.append(f"{area_id}: unknown canonical territory {territory_id}")

    if len(areas) != 14:
        errors.append(f"expected 14 proposed macro-areas, found {len(areas)}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(f"ERROR: {problem}" for problem in problems))
        sys.exit(1)
    print("PASS: engineering organization crosswalk is structurally valid")
