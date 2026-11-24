"""Small, dependency-free semantic model validator for EKTA UMSF 0.1."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Iterable


@dataclass(frozen=True)
class SemanticAddress:
    """A view-relative semantic address, not a Cartesian coordinate."""

    x_layer_id: str
    y_module_id: str
    z_depth: int
    valid_from: str
    valid_to: str | None = None

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.x_layer_id.strip():
            errors.append("x_layer_id must be non-empty")
        if not self.y_module_id.strip():
            errors.append("y_module_id must be non-empty")
        if isinstance(self.z_depth, bool) or not isinstance(self.z_depth, int) or self.z_depth < 0:
            errors.append("z_depth must be a non-negative integer")
        start = _parse_aware_datetime(self.valid_from, "valid_from", errors)
        end = None
        if self.valid_to is not None:
            end = _parse_aware_datetime(self.valid_to, "valid_to", errors)
        if start is not None and end is not None and end <= start:
            errors.append("valid_to must be later than valid_from")
        return errors


@dataclass(frozen=True)
class Entity:
    id: str
    type: str
    name: str
    addresses: tuple[SemanticAddress, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Relationship:
    source_id: str
    predicate: str
    target_id: str
    context: str | None = None
    status: str = "PROPOSED"


@dataclass(frozen=True)
class SystemModel:
    model_id: str
    root_entity_id: str
    view_id: str
    entities: tuple[Entity, ...]
    relationships: tuple[Relationship, ...] = ()


def _parse_aware_datetime(value: str, field_name: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field_name} must be a non-empty ISO 8601 timestamp")
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{field_name} must be a valid ISO 8601 timestamp")
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        errors.append(f"{field_name} must include a timezone offset")
        return None
    return parsed


def validate_model(
    model: SystemModel,
    known_layer_ids: Iterable[str] | None = None,
    known_predicates: Iterable[str] | None = None,
) -> list[str]:
    """Return deterministic validation errors; never mutate or promote source data."""
    errors: list[str] = []
    if not model.model_id.strip():
        errors.append("model_id must be non-empty")
    if not model.root_entity_id.strip():
        errors.append("root_entity_id must be non-empty")
    if not model.view_id.strip():
        errors.append("view_id must be non-empty")

    by_id: dict[str, Entity] = {}
    for entity in model.entities:
        if not entity.id.strip():
            errors.append("entity id must be non-empty")
            continue
        if entity.id in by_id:
            errors.append(f"duplicate entity id: {entity.id}")
        else:
            by_id[entity.id] = entity
        if not entity.type.strip():
            errors.append(f"{entity.id}: type must be non-empty")
        if not entity.name.strip():
            errors.append(f"{entity.id}: name must be non-empty")
        for index, address in enumerate(entity.addresses):
            for problem in address.validate():
                errors.append(f"{entity.id}: address[{index}]: {problem}")
            if known_layer_ids is not None and address.x_layer_id not in set(known_layer_ids):
                errors.append(f"{entity.id}: unknown layer id: {address.x_layer_id}")

    if model.root_entity_id not in by_id:
        errors.append(f"root entity not found: {model.root_entity_id}")

    predicates = set(known_predicates) if known_predicates is not None else None
    for index, relation in enumerate(model.relationships):
        if relation.source_id not in by_id:
            errors.append(f"relationship[{index}]: source not found: {relation.source_id}")
        if relation.target_id not in by_id:
            errors.append(f"relationship[{index}]: target not found: {relation.target_id}")
        if not relation.predicate.strip():
            errors.append(f"relationship[{index}]: predicate must be non-empty")
        elif predicates is not None and relation.predicate not in predicates:
            errors.append(f"relationship[{index}]: unknown predicate: {relation.predicate}")
    return errors


def model_to_dict(model: SystemModel) -> dict[str, Any]:
    """Serialize the model into the UMSF 0.1 JSON-compatible shape."""
    return {
        "schema_version": "0.1.0",
        "model_id": model.model_id,
        "root_entity_id": model.root_entity_id,
        "view_id": model.view_id,
        "entities": [
            {
                "id": entity.id,
                "type": entity.type,
                "name": entity.name,
                "addresses": [
                    {
                        "x_layer_id": address.x_layer_id,
                        "y_module_id": address.y_module_id,
                        "z_depth": address.z_depth,
                        "valid_from": address.valid_from,
                        "valid_to": address.valid_to,
                    }
                    for address in entity.addresses
                ],
                "metadata": dict(entity.metadata),
            }
            for entity in model.entities
        ],
        "relationships": [
            {
                "source_id": edge.source_id,
                "predicate": edge.predicate,
                "target_id": edge.target_id,
                "context": edge.context,
                "status": edge.status,
            }
            for edge in model.relationships
        ],
        "provenance": [],
    }
