"""Repository facade and search service over EKTA's Git-native source of truth."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from .content import load_concepts, load_yaml_file
from .graph import build_graph
from .search import (
    SearchPlan,
    _snippet,
    WORD_PATTERN,
    load_documents,
    normalize,
    parse_query,
    slug,
)


class AtlasRepository:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.records = load_concepts(self.root)
        self.by_id = {record.id: record for record in self.records}
        self.documents = load_documents(self.root)
        self.documents_by_id = {document.id: document for document in self.documents}

        self._domains = load_yaml_file(self.root / "taxonomy" / "domains.yml")
        self._territories = load_yaml_file(self.root / "taxonomy" / "territories.yml")
        self._layers = load_yaml_file(self.root / "taxonomy" / "layers.yml")
        self._knowledge_types = load_yaml_file(self.root / "taxonomy" / "knowledge-types.yml")
        relation_doc = load_yaml_file(self.root / "taxonomy" / "relations.yml")
        self.relations = set(relation_doc.get("relations", []))
        self.graph_data = build_graph(self.records, self.relations)

        self.domain_labels = {
            item["id"]: item.get("label", item["id"])
            for item in self._domains.get("domains", [])
            if isinstance(item, dict) and item.get("id")
        }
        self.layer_labels = {
            item["id"]: item.get("label", item["id"])
            for item in self._layers.get("layers", [])
            if isinstance(item, dict) and item.get("id")
        }
        self.territory_labels = {
            item["id"]: item.get("label", item["id"])
            for item in self._territories.get("territories", [])
            if isinstance(item, dict) and item.get("id")
        }
        self.domain_to_territories: dict[str, set[str]] = {}
        for territory in self._territories.get("territories", []):
            if not isinstance(territory, dict):
                continue
            for domain_id in territory.get("domain_ids", []):
                self.domain_to_territories.setdefault(domain_id, set()).add(territory["id"])

    def list_concepts(
        self,
        query: str | None = None,
        domain: str | None = None,
        layer: str | None = None,
        status: str | None = None,
    ) -> list[dict[str, Any]]:
        needle = normalize(query or "")
        result = []
        for record in self.records:
            searchable = normalize(" ".join((
                record.id, record.canonical_name, *record.aliases, record.body
            )))
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

    def _concept_fields(self, record: Any) -> dict[str, Any]:
        domains = list(record.domains)
        layers = list(record.layers)
        types = list(record.knowledge_types)
        aliases = list(record.aliases)
        metadata = record.metadata
        tags = set(slug(value) for value in (
            record.id, record.canonical_name, *aliases, *domains, *layers, *types,
            record.status, *_as_list(metadata.get("tags")), *_as_list(metadata.get("keywords"))
        ) if slug(value))
        tags.update(slug(self.domain_labels.get(value, value)) for value in domains)
        tags.update(slug(self.layer_labels.get(value, value)) for value in layers)
        tag_sources = (record.canonical_name, *aliases, *domains, *layers, *types)
        stop_tags = {"the", "and", "for", "with", "from", "into"}
        for tag_source in tag_sources:
            tags.update(
                slug(word) for word in WORD_PATTERN.findall(tag_source)
                if len(word) > 2 and slug(word) not in stop_tags
            )
        territories = sorted({
            territory_id
            for domain_id in domains
            for territory_id in self.domain_to_territories.get(domain_id, set())
        })
        territory_labels = [self.territory_labels.get(value, value) for value in territories]
        tags.update(slug(value) for value in (*territories, *territory_labels))
        headings = [
            line.lstrip("#").strip()
            for line in record.body.splitlines()
            if line.startswith("#") and line.lstrip("#").strip()
        ]
        definition = self._section_excerpt(record.body, "Definition")
        fields = {
            "id": record.id,
            "kind": "concept",
            "title": record.canonical_name,
            "status": record.status,
            "revision": record.revision,
            "domains": domains,
            "domain_labels": [self.domain_labels.get(value, value) for value in domains],
            "layers": layers,
            "layer_labels": [self.layer_labels.get(value, value) for value in layers],
            "territories": territories,
            "territory_labels": territory_labels,
            "knowledge_types": types,
            "aliases": aliases,
            "tags": sorted(tags),
            "headings": headings,
            "content": record.body,
            "source_file": record.source_file,
            "summary": definition,
        }
        return fields

    @staticmethod
    def _section_excerpt(body: str, section_name: str) -> str:
        lines = body.splitlines()
        active = False
        collected: list[str] = []
        for line in lines:
            if line.startswith("## "):
                if active:
                    break
                active = line[3:].strip().casefold() == section_name.casefold()
                continue
            if active and line.strip():
                collected.append(line.strip())
        return " ".join(collected)[:420]

    def _document_fields(self, document: Any) -> dict[str, Any]:
        return {
            "id": document.id,
            "kind": document.kind,
            "title": document.title,
            "status": None,
            "revision": None,
            "domains": [],
            "domain_labels": [],
            "layers": [],
            "layer_labels": [],
            "knowledge_types": [],
            "aliases": [],
            "tags": list(document.tags),
            "headings": list(document.headings),
            "content": document.content,
            "source_file": document.source_file,
            "summary": document.headings[1] if len(document.headings) > 1 else document.content[:360],
        }

    @staticmethod
    def _field_match(field: str, value: str, item: dict[str, Any]) -> bool:
        needle = normalize(value)
        needle_slug = slug(value)
        if field == "id":
            return normalize(item["id"]) == needle or normalize(item["id"]).startswith(needle)
        if field == "domain":
            candidates = item.get("domains", []) + item.get("domain_labels", [])
        elif field == "layer":
            candidates = item.get("layers", []) + item.get("layer_labels", [])
        elif field == "territory":
            candidates = item.get("territories", []) + item.get("territory_labels", [])
        elif field == "type":
            candidates = item.get("knowledge_types", [])
        elif field == "status":
            candidates = [item.get("status") or ""]
        elif field == "kind":
            candidates = [item.get("kind") or ""]
        elif field == "tag":
            candidates = item.get("tags", [])
        else:
            return True
        return any(normalize(candidate) == needle or slug(candidate) == needle_slug for candidate in candidates)

    @staticmethod
    def _term_score(term: str, item: dict[str, Any]) -> tuple[int, str | None]:
        fields = (
            ("id", item.get("id", ""), 115),
            ("title", item.get("title", ""), 100),
            ("aliases", " ".join(item.get("aliases", [])), 82),
            ("tags", " ".join(item.get("tags", [])), 72),
            ("headings", " ".join(item.get("headings", [])), 58),
            ("summary", item.get("summary", ""), 35),
            ("content", item.get("content", ""), 12),
            ("source_file", item.get("source_file", ""), 18),
        )
        best_score = 0
        best_field: str | None = None
        for field, raw_value, weight in fields:
            value = normalize(raw_value)
            if not value or term not in value:
                continue
            score = weight + (20 if value == term else 8 if value.startswith(term) else 0)
            if score > best_score:
                best_score, best_field = score, field
        return best_score, best_field

    def search(
        self,
        query: str = "",
        *,
        domain: str | None = None,
        layer: str | None = None,
        knowledge_type: str | None = None,
        status: str | None = None,
        kind: str | None = None,
        territory: str | None = None,
        limit: int = 30,
        offset: int = 0,
    ) -> dict[str, Any]:
        plan = parse_query(query)
        extra_filters = {
            key: value for key, value in {
                "domain": domain, "layer": layer, "type": knowledge_type,
                "status": status, "kind": kind, "territory": territory,
            }.items() if value
        }
        all_filters: dict[str, tuple[str, ...]] = dict(plan.filters)
        for key, value in extra_filters.items():
            all_filters[key] = (*all_filters.get(key, ()), value)

        candidates = [self._concept_fields(record) for record in self.records]
        candidates.extend(self._document_fields(document) for document in self.documents)

        ranked: list[dict[str, Any]] = []
        text_needles = (*plan.terms, *plan.phrases)
        for item in candidates:
            if any(
                not self._field_match(field, value, item)
                for field, values in all_filters.items()
                for value in values
            ):
                continue
            if any(tag not in item.get("tags", []) for tag in plan.hashtags):
                continue

            score = 0
            matched_fields: set[str] = set()
            valid = True
            for phrase in plan.phrases:
                phrase_score, phrase_field = self._term_score(phrase, item)
                if not phrase_score:
                    valid = False
                    break
                score += phrase_score + 12
                matched_fields.add(phrase_field or "content")
            if not valid:
                continue

            for term in plan.terms:
                term_score, term_field = self._term_score(term, item)
                if not term_score:
                    valid = False
                    break
                score += term_score
                matched_fields.add(term_field or "content")
            if not valid:
                continue

            if plan.hashtags:
                score += 70 * len(plan.hashtags)
                matched_fields.add("hashtags")
            if all_filters:
                score += 30 * sum(len(values) for values in all_filters.values())
                matched_fields.add("filters")
            if not text_needles and not plan.hashtags and not all_filters:
                score = 1
            excerpt = _snippet(item.get("content", ""), text_needles or plan.hashtags or [item["title"]])
            result = {
                key: value for key, value in item.items()
                if key not in {"content", "headings"}
            }
            result.update({
                "score": score,
                "matched_fields": sorted(matched_fields),
                "snippet": excerpt or item.get("summary", ""),
                "headings": item.get("headings", [])[:8],
            })
            ranked.append(result)

        ranked.sort(key=lambda item: (-item["score"], item["kind"], normalize(item["title"])))
        total = len(ranked)
        return {
            "query": query,
            "filters": {key: list(values) for key, values in all_filters.items()},
            "hashtags": list(plan.hashtags),
            "count": total,
            "offset": max(offset, 0),
            "limit": min(max(limit, 1), 100),
            "has_more": offset + min(max(limit, 1), 100) < total,
            "results": ranked[max(offset, 0):max(offset, 0) + min(max(limit, 1), 100)],
        }

    def get_document(self, document_id: str) -> dict[str, Any] | None:
        document = self.documents_by_id.get(document_id)
        if document is None:
            return None
        return {
            "id": document.id,
            "title": document.title,
            "kind": document.kind,
            "source_file": document.source_file,
            "tags": list(document.tags),
            "headings": list(document.headings),
            "content": document.content,
        }

    def relationships_for(self, concept_id: str) -> dict[str, list[dict[str, Any]]]:
        return {
            "outgoing": [edge for edge in self.graph_data["edges"] if edge["source"] == concept_id],
            "incoming": [edge for edge in self.graph_data["edges"] if edge.get("target") == concept_id],
        }

    def facets(self) -> dict[str, Any]:
        domain_counts: Counter[str] = Counter()
        layer_counts: Counter[str] = Counter()
        type_counts: Counter[str] = Counter()
        status_counts: Counter[str] = Counter()
        tag_counts: Counter[str] = Counter()
        territory_counts: Counter[str] = Counter()
        for record in self.records:
            domain_counts.update(record.domains)
            layer_counts.update(record.layers)
            type_counts.update(record.knowledge_types)
            status_counts.update([record.status])
            field_data = self._concept_fields(record)
            territory_counts.update(set(field_data["territories"]))
            tag_counts.update(set(field_data["tags"]))
        for document in self.documents:
            tag_counts.update(set(document.tags))

        return {
            "domains": [
                {"id": item["id"], "label": item.get("label", item["id"]), "count": domain_counts[item["id"]]}
                for item in self._domains.get("domains", [])
                if isinstance(item, dict) and item.get("id")
            ],
            "layers": [
                {"id": item["id"], "label": item.get("label", item["id"]), "count": layer_counts[item["id"]]}
                for item in self._layers.get("layers", [])
                if isinstance(item, dict) and item.get("id")
            ],
            "territories": [
                {"id": item["id"], "label": item.get("label", item["id"]),
                 "count": territory_counts[item["id"]]}
                for item in self._territories.get("territories", [])
                if isinstance(item, dict) and item.get("id")
            ],
            "knowledge_types": [
                {"id": value, "label": value.replace("-", " ").title(), "count": type_counts[value]}
                for value in self._knowledge_types.get("knowledge_types", [])
            ],
            "statuses": [
                {"id": value, "label": value, "count": count}
                for value, count in sorted(status_counts.items())
            ],
            "tags": [tag for tag, _ in tag_counts.most_common(80)],
        }

    def get_concept(self, concept_id: str) -> dict[str, Any] | None:
        record = self.by_id.get(concept_id)
        if record is None:
            return None
        result = self.serialize_concept(record, include_body=True)
        result["relationships"] = self.relationships_for(concept_id)
        return result

    def serialize_concept(self, record: Any, include_body: bool) -> dict[str, Any]:
        result = {
            "id": record.id,
            "canonical_name": record.canonical_name,
            "status": record.status,
            "revision": record.revision,
            "domains": list(record.domains),
            "territories": sorted({
                territory_id
                for domain_id in record.domains
                for territory_id in self.domain_to_territories.get(domain_id, set())
            }),
            "territory_labels": [
                self.territory_labels[territory_id]
                for territory_id in sorted({
                    territory_id
                    for domain_id in record.domains
                    for territory_id in self.domain_to_territories.get(domain_id, set())
                })
            ],
            "layers": list(record.layers),
            "knowledge_types": list(record.knowledge_types),
            "aliases": list(record.aliases),
            "tags": list(record.metadata.get("tags", [])),
            "source_file": record.source_file,
        }
        if include_body:
            result["body"] = record.body
            result["metadata"] = record.metadata
        return result

    def taxonomy(self) -> dict[str, Any]:
        return {
            "domains": self._domains,
            "territories": self._territories,
            "layers": self._layers,
            "knowledge_types": self._knowledge_types,
            "relations": sorted(self.relations),
        }

    def overview(self) -> dict[str, Any]:
        graph_summary = self.graph_data["summary"]
        return {
            "product": "Engineering Knowledge & Techniques Atlas",
            "runtime_version": "0.2.0",
            "source_of_truth": "Git-native Markdown/YAML",
            "concept_count": len(self.records),
            "document_count": len(self.documents),
            "searchable_item_count": len(self.records) + len(self.documents),
            "domain_count": len(self._domains.get("domains", [])),
            "territory_count": len(self._territories.get("territories", [])),
            "layer_count": len(self._layers.get("layers", [])),
            "relation_vocabulary_count": len(self.relations),
            "graph": graph_summary,
            "content_status": "search_and_explore_bootstrap",
        }


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(item) for item in value]
    return [str(value)]
