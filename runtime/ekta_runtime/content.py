"""Load canonical EKTA Markdown/YAML records without mutating source files."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ConceptRecord:
    id: str
    canonical_name: str
    status: str
    revision: str
    domains: tuple[str, ...]
    layers: tuple[str, ...]
    knowledge_types: tuple[str, ...]
    aliases: tuple[str, ...]
    source_file: str
    body: str
    metadata: dict[str, Any]


class ContentError(ValueError):
    """Raised when canonical content cannot be parsed safely."""


def _normalize_yaml_dates(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, list):
        return [_normalize_yaml_dates(item) for item in value]
    if isinstance(value, dict):
        return {key: _normalize_yaml_dates(item) for key, item in value.items()}
    return value


def split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ContentError("Missing YAML front matter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ContentError("Front matter must be closed by a second --- delimiter")
    try:
        metadata = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise ContentError(f"Invalid YAML front matter: {exc}") from exc
    if not isinstance(metadata, dict):
        raise ContentError("Front matter must be a YAML mapping")
    return _normalize_yaml_dates(metadata), parts[2].lstrip("\n")


def _strings(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ContentError("Expected a YAML list")
    return tuple(str(item).strip() for item in value if str(item).strip())


def load_concepts(root: Path) -> list[ConceptRecord]:
    directory = root / "encyclopedia" / "concepts"
    if not directory.exists():
        return []
    records: list[ConceptRecord] = []
    for path in sorted(directory.glob("*.md")):
        metadata, body = split_front_matter(path.read_text(encoding="utf-8"))
        required = ("id", "canonical_name", "status", "revision")
        missing = [key for key in required if not metadata.get(key)]
        if missing:
            raise ContentError(f"{path}: missing required metadata: {', '.join(missing)}")
        records.append(ConceptRecord(
            id=str(metadata["id"]),
            canonical_name=str(metadata["canonical_name"]),
            status=str(metadata["status"]),
            revision=str(metadata["revision"]),
            domains=_strings(metadata.get("domains", [])),
            layers=_strings(metadata.get("layers", [])),
            knowledge_types=_strings(metadata.get("knowledge_types", [])),
            aliases=_strings(metadata.get("aliases", [])),
            source_file=path.relative_to(root).as_posix(),
            body=body,
            metadata=metadata,
        ))
    return records


def load_yaml_file(path: Path) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ContentError(f"{path}: invalid YAML: {exc}") from exc
    if not isinstance(value, dict):
        raise ContentError(f"{path}: expected a YAML mapping")
    return value
