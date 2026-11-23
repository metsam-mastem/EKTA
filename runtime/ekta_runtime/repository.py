"""Read-only repository facade over EKTA's Git-native source of truth."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .content import load_concepts, load_yaml_file
from .graph import build_graph


class AtlasRepository:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.records = load_concepts(self.root)
        self.by_id = {record.id: record for record in self.records}
        relation_doc = load_yaml_file(self.root / "taxonomy" / "relations.yml")
        self.relations = set(relation_doc.get("relations", []))
        self.graph_data = build_graph(self.records, self.relations)

    def list_concepts(
        self,
        query: str | None = None,
        domain: str | None = None,
        layer: str | None = None,
        status: str | None = None,
    ) -> list[dict[str, Any]]:
        needle = (query or "").strip().casefold()
        result = []
        for record in self.records:
            searchable = " ".join((
                record.id, record.canonical_name, *record.aliases, record.body
            )).casefold()
            if needle and needle not in searchable:
                continue
            if domain and domain not in record.domains:
                continue
            if layer and layer not in record.layers:
                continue
            if status and status.casefold() != record.status.casefold():
                continue
            result.append(self.serialize_concept(record, include_body=False))
        return result

    def get_concept(self, concept_id: str) -> dict[str, Any] | None:
        record = self.by_id.get(concept_id)
        return self.serialize_concept(record, include_body=True) if record else None

    @staticmethod
    def serialize_concept(record: Any, include_body: bool) -> dict[str, Any]:
        result = {
            "id": record.id,
            "canonical_name": record.canonical_name,
            "status": record.status,
            "revision": record.revision,
            "domains": list(record.domains),
            "layers": list(record.layers),
            "knowledge_types": list(record.knowledge_types),
            "aliases": list(record.aliases),
            "source_file": record.source_file,
        }
        if include_body:
            result["body"] = record.body
            result["metadata"] = record.metadata
        return result

    def taxonomy(self) -> dict[str, Any]:
        return {
            "domains": load_yaml_file(self.root / "taxonomy" / "domains.yml"),
            "layers": load_yaml_file(self.root / "taxonomy" / "layers.yml"),
            "knowledge_types": load_yaml_file(self.root / "taxonomy" / "knowledge-types.yml"),
            "relations": sorted(self.relations),
        }

    def overview(self) -> dict[str, Any]:
        graph_summary = self.graph_data["summary"]
        return {
            "product": "Engineering Knowledge & Techniques Atlas",
            "runtime_version": "0.1.0",
            "source_of_truth": "Git-native Markdown/YAML",
            "concept_count": len(self.records),
            "domain_count": len(self.taxonomy()["domains"].get("domains", [])),
            "layer_count": len(self.taxonomy()["layers"].get("layers", [])),
            "relation_vocabulary_count": len(self.relations),
            "graph": graph_summary,
            "content_status": "read_only_bootstrap",
        }
