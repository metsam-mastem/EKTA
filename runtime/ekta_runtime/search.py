"""Unified free-text, hashtag, and fielded search over EKTA content."""
from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .content import ConceptRecord


FIELD_PATTERN = re.compile(
    r"(?<!\S)(id|domain|layer|type|status|kind|tag):"
    r'(?:"([^"]+)"|\'([^\']+)\'|(\S+))',
    re.IGNORECASE,
)
HASHTAG_PATTERN = re.compile(r"(?<![\w#])#([\w-]+)", re.UNICODE)
WORD_PATTERN = re.compile(r"[\w]+(?:-[\w]+)*", re.UNICODE)
INDEXED_EXTENSIONS = {".md", ".yml", ".yaml", ".json"}
INDEXED_ROOTS = {
    "docs", "maps", "references", "research", "taxonomy", "schemas",
    "templates", "decision-lab", "workflows",
}
INDEXED_ROOT_FILES = {
    "README.md", "CONTRIBUTING.md", "GOVERNANCE.md", "LICENSE-STATUS.md",
    "CHANGELOG.md",
}


@dataclass(frozen=True)
class SearchPlan:
    terms: tuple[str, ...]
    phrases: tuple[str, ...]
    hashtags: tuple[str, ...]
    filters: dict[str, tuple[str, ...]]


@dataclass(frozen=True)
class DocumentRecord:
    id: str
    title: str
    source_file: str
    kind: str
    content: str
    tags: tuple[str, ...]
    headings: tuple[str, ...]


def normalize(value: str) -> str:
    """Normalize Arabic/Persian glyph variants and Unicode for stable matching."""
    value = unicodedata.normalize("NFKC", str(value)).casefold()
    value = value.replace("ي", "ی").replace("ى", "ی").replace("ك", "ک")
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"\s+", " ", value).strip()


def slug(value: str) -> str:
    value = normalize(value).replace("_", "-")
    return re.sub(r"[^\w]+", "-", value, flags=re.UNICODE).strip("-")


def parse_query(query: str) -> SearchPlan:
    remaining = query or ""
    filters: dict[str, list[str]] = {}
    for match in FIELD_PATTERN.finditer(remaining):
        field = match.group(1).casefold()
        value = next((item for item in match.groups()[1:] if item is not None), "")
        filters.setdefault(field, []).append(value.strip())
    remaining = FIELD_PATTERN.sub(" ", remaining)

    hashtags = tuple(
        dict.fromkeys(slug(item) for item in HASHTAG_PATTERN.findall(remaining) if slug(item))
    )
    remaining = HASHTAG_PATTERN.sub(" ", remaining)

    phrases: list[str] = []
    for match in re.finditer(r'"([^"]+)"|\'([^\']+)\'', remaining):
        value = next(item for item in match.groups() if item is not None)
        if normalize(value):
            phrases.append(normalize(value))
    remaining = re.sub(r'"[^"]+"|\'[^\']+\'', " ", remaining)

    terms = tuple(dict.fromkeys(normalize(item) for item in WORD_PATTERN.findall(remaining) if normalize(item)))
    return SearchPlan(
        terms=terms,
        phrases=tuple(dict.fromkeys(phrases)),
        hashtags=hashtags,
        filters={key: tuple(values) for key, values in filters.items()},
    )


def load_documents(root: Path) -> list[DocumentRecord]:
    records: list[DocumentRecord] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in INDEXED_EXTENSIONS:
            continue
        relative = path.relative_to(root)
        if any(part.startswith(".") or part in {"node_modules", ".venv", "__pycache__", "build", "dist"} for part in relative.parts):
            continue
        if relative.parts[0] not in INDEXED_ROOTS and relative.as_posix() not in INDEXED_ROOT_FILES:
            continue
        if relative.parts[:2] == ("encyclopedia", "concepts"):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        headings = tuple(
            line.lstrip("#").strip()
            for line in content.splitlines()
            if line.startswith("#") and line.lstrip("#").strip()
        )
        title = headings[0] if headings else path.stem.replace("-", " ").replace("_", " ").title()
        suffix = hashlib.sha256(relative.as_posix().encode("utf-8")).hexdigest()[:12]
        doc_id = f"EKTA-DOC-{suffix}"
        tag_values: set[str] = set()
        for part in relative.parts[:-1]:
            if part not in {".", ""}:
                tag_values.add(slug(part))
        tag_values.add(slug(path.stem))
        for heading in headings[:12]:
            heading_slug = slug(heading)
            if heading_slug:
                tag_values.add(heading_slug)
        for line in content.splitlines():
            if line.lstrip().startswith("#"):
                continue
            tag_values.update(slug(tag) for tag in HASHTAG_PATTERN.findall(line))
        kind = "taxonomy" if relative.parts[0] == "taxonomy" else (
            "schema" if relative.parts[0] == "schemas" else "document"
        )
        records.append(DocumentRecord(
            id=doc_id,
            title=title,
            source_file=relative.as_posix(),
            kind=kind,
            content=content,
            tags=tuple(sorted(tag for tag in tag_values if tag)),
            headings=headings,
        ))
    return records


def _as_strings(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, (list, tuple, set)):
        return tuple(str(item) for item in value)
    return (str(value),)


def _snippet(content: str, needles: Iterable[str], length: int = 240) -> str:
    plain = re.sub(r"\s+", " ", content).strip()
    normalized = normalize(plain)
    positions = [normalized.find(normalize(needle)) for needle in needles if normalize(needle)]
    positions = [position for position in positions if position >= 0]
    start = max(0, (min(positions) - 75)) if positions else 0
    fragment = plain[start:start + length]
    if start:
        fragment = "…" + fragment
    if start + length < len(plain):
        fragment += "…"
    return fragment
