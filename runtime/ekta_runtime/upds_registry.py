"""Read-only repository-backed registry for UPDS document records."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema
import yaml


class RegistryError(ValueError):
    """Raised when canonical UPDS records cannot be read or validated."""


class DocumentRegistry:
    """Loads and validates project-document records from the Git-native store.

    This first vertical slice is intentionally read-only. It never writes files,
    changes canonical records, or accepts filesystem paths from API callers.
    """

    def __init__(self, root: Path | str):
        self.root = Path(root).resolve()
        self.schema_path = self.root / "schemas" / "upds-document.schema.json"
        self.records_dir = self.root / "upds" / "records"

    def list_documents(self) -> list[dict[str, Any]]:
        if not self.schema_path.is_file():
            raise RegistryError("UPDS document schema is missing")

        try:
            schema = json.loads(self.schema_path.read_text(encoding="utf-8"))
            jsonschema.Draft202012Validator.check_schema(schema)
        except (OSError, json.JSONDecodeError, jsonschema.SchemaError) as exc:
            raise RegistryError(f"UPDS document schema is invalid: {exc}") from exc

        validator = jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )
        if not self.records_dir.exists():
            return []

        records: list[dict[str, Any]] = []
        errors: list[str] = []
        seen_ids: set[str] = set()
        records_root = self.records_dir.resolve()

        for path in sorted(self.records_dir.rglob("*.yml")) + sorted(self.records_dir.rglob("*.yaml")):
            try:
                resolved = path.resolve(strict=True)
                if not resolved.is_relative_to(records_root) or not resolved.is_file():
                    errors.append(f"{path}: record path escapes UPDS records directory")
                    continue
                record = yaml.safe_load(resolved.read_text(encoding="utf-8"))
            except yaml.YAMLError as exc:
                errors.append(f"{path}: invalid YAML: {exc}")
                continue
            except OSError as exc:
                errors.append(f"{path}: cannot read record: {exc}")
                continue

            if not isinstance(record, dict):
                errors.append(f"{path}: record must be a YAML mapping")
                continue

            for issue in sorted(validator.iter_errors(record), key=lambda err: list(err.path)):
                location = ".".join(str(part) for part in issue.path) or "record"
                errors.append(f"{path}: schema error at {location}: {issue.message}")

            record_id = record.get("id")
            if isinstance(record_id, str):
                if record_id in seen_ids:
                    errors.append(f"duplicate document ID: {record_id}")
                seen_ids.add(record_id)
            records.append(record)

        if errors:
            raise RegistryError("; ".join(errors))

        return sorted(records, key=lambda item: item["id"])

    def get_document(self, document_id: str) -> dict[str, Any] | None:
        for record in self.list_documents():
            if record["id"] == document_id:
                return record
        return None
