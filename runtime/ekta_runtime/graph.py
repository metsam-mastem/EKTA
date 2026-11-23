"""Build a typed, traceable graph from canonical concept records."""
from __future__ import annotations

import re
from typing import Any

from .content import ConceptRecord

RELATION_LINE = re.compile(r"^\s*-\s*([A-Z][A-Z0-9_]*):\s*(.+?)\s*$")


def _key(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


def extract_relationships(body: str) -> list[tuple[str, str]]:
    in_section = False
    found: list[tuple[str, str]] = []
    for line in body.splitlines():
        heading = line.strip()
        if heading.startswith("#"):
            in_section = heading.casefold() in {"## relationships", "## relationships and links"}
            continue
        if not in_section:
            continue
        match = RELATION_LINE.match(line)
        if match:
            found.append((match.group(1), match.group(2).strip().strip("`'\\")))
    return found


def build_graph(records: list[ConceptRecord], relation_registry: set[str]) -> dict[str, Any]:
    by_name: dict[str, str] = {}
    for record in records:
        for label in (record.canonical_name, *record.aliases, record.id):
            by_name[_key(label)] = record.id

    nodes = [{
        "id": item.id,
        "label": item.canonical_name,
        "status": item.status,
        "revision": item.revision,
        "domains": list(item.domains),
        "layers": list(item.layers),
        "knowledge_types": list(item.knowledge_types),
        "source_file": item.source_file,
    } for item in records]

    edges: list[dict[str, Any]] = []
    for record in records:
        for predicate, target_label in extract_relationships(record.body):
            target_id = by_name.get(_key(target_label))
            predicate_valid = predicate in relation_registry
            edges.append({
                "id": f"{record.id}:{predicate}:{target_id or _key(target_label)}",
                "source": record.id,
                "predicate": predicate,
                "target": target_id,
                "target_label": target_label,
                "status": "resolved" if target_id and predicate_valid else (
                    "invalid_predicate" if not predicate_valid else "unresolved_target"
                ),
                "source_file": record.source_file,
            })

    return {
        "schema_version": 1,
        "generator": "ekta-runtime",
        "nodes": nodes,
        "edges": edges,
        "summary": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "resolved_edge_count": sum(edge["status"] == "resolved" for edge in edges),
            "unresolved_edge_count": sum(edge["status"] != "resolved" for edge in edges),
        },
    }
