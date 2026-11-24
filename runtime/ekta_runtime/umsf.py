"""Small, dependency-free semantic model validator for EKTA UMSF 0.1."""
from __future__ import annotations

from collections.abc import Mapping
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
        if not isinstance(self.x_layer_id, str) or not self.x_layer_id.strip():
            errors.append("x_layer_id must be non-empty")
        if not isinstance(self.y_module_id, str) or not self.y_module_id.strip():
            errors.append("y_module_id must be non-empty")
        if isinstance(self.z_depth, bool) or not isinstance(self.z_depth, int) or self.z_depth < 0:
            errors.append("z_depth must be a non-negative integer")
        start = _parse_aware_datetime(self.valid_from, "valid_from", errors)
        end = _parse_aware_datetime(self.valid_to, "valid_to", errors) if self.valid_to is not None else None
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
    provenance: tuple[dict[str, Any], ...] = ()


def _parse_aware_datetime(value: Any, field_name: str, errors: list[str]) -> datetime | None:
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


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_model(
    model: SystemModel,
    known_layer_ids: Iterable[str] | None = None,
    known_predicates: Iterable[str] | None = None,
) -> list[str]:
    """Return deterministic validation errors; malformed input must not crash validation."""
    if not isinstance(model, SystemModel):
        return ["model must be a SystemModel instance"]

    errors: list[str] = []
    for field_name in ("model_id", "root_entity_id", "view_id"):
        if not _non_empty_string(getattr(model, field_name)):
            errors.append(f"{field_name} must be non-empty")

    layer_ids = set(known_layer_ids) if known_layer_ids is not None else None
    predicates = set(known_predicates) if known_predicates is not None else None
    if not isinstance(model.entities, tuple):
        return errors + ["entities must be a tuple"]
    by_id: dict[str, Entity] = {}
    for index, entity in enumerate(model.entities):
        if not isinstance(entity, Entity):
            errors.append(f"entities[{index}] must be an Entity")
            continue
        if not _non_empty_string(entity.id):
            errors.append(f"entities[{index}].id must be non-empty")
            continue
        if entity.id in by_id:
            errors.append(f"duplicate entity id: {entity.id}")
        else:
            by_id[entity.id] = entity
        if not _non_empty_string(entity.type):
            errors.append(f"{entity.id}: type must be non-empty")
        if not _non_empty_string(entity.name):
            errors.append(f"{entity.id}: name must be non-empty")
        if not isinstance(entity.addresses, tuple):
            errors.append(f"{entity.id}: addresses must be a tuple")
            continue
        for address_index, address in enumerate(entity.addresses):
            if not isinstance(address, SemanticAddress):
                errors.append(f"{entity.id}: address[{address_index}] must be a SemanticAddress")
                continue
            for problem in address.validate():
                errors.append(f"{entity.id}: address[{address_index}]: {problem}")
            if layer_ids is not None and _non_empty_string(address.x_layer_id) and address.x_layer_id not in layer_ids:
                errors.append(f"{entity.id}: unknown layer id: {address.x_layer_id}")

    if _non_empty_string(model.root_entity_id) and model.root_entity_id not in by_id:
        errors.append(f"root entity not found: {model.root_entity_id}")

    if not isinstance(model.relationships, tuple):
        return errors + ["relationships must be a tuple"]
    for index, relation in enumerate(model.relationships):
        if not isinstance(relation, Relationship):
            errors.append(f"relationships[{index}] must be a Relationship")
            continue
        if relation.source_id not in by_id:
            errors.append(f"relationship[{index}]: source not found: {relation.source_id}")
        if relation.target_id not in by_id:
            errors.append(f"relationship[{index}]: target not found: {relation.target_id}")
        if not _non_empty_string(relation.predicate):
            errors.append(f"relationship[{index}]: predicate must be non-empty")
        elif predicates is not None and relation.predicate not in predicates:
            errors.append(f"relationship[{index}]: unknown predicate: {relation.predicate}")
    return errors


def model_to_dict(model: SystemModel) -> dict[str, Any]:
    """Serialize the model into the UMSF 0.1 JSON-compatible shape."""
    if not isinstance(model, SystemModel):
        raise TypeError("model must be a SystemModel instance")
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
                **{
                    "source_id": edge.source_id,
                    "predicate": edge.predicate,
                    "target_id": edge.target_id,
                    "status": edge.status,
                },
                **({"context": edge.context} if edge.context is not None else {}),
            }
            for edge in model.relationships
        ],
        "provenance": [dict(item) for item in model.provenance],
    }


def model_from_dict(data: Mapping[str, Any]) -> SystemModel:
    """Parse a UMSF JSON-compatible mapping without discarding provenance."""
    if not isinstance(data, Mapping):
        raise TypeError("UMSF model data must be a mapping")
    if data.get("schema_version") != "0.1.0":
        raise ValueError("unsupported UMSF schema_version; expected 0.1.0")
    for key in ("model_id", "root_entity_id", "view_id", "entities", "relationships"):
        if key not in data:
            raise ValueError(f"missing required UMSF field: {key}")
    if not all(_non_empty_string(data[key]) for key in ("model_id", "root_entity_id", "view_id")):
        raise ValueError("model_id, root_entity_id, and view_id must be non-empty strings")
    if not isinstance(data["entities"], list) or not isinstance(data["relationships"], list):
        raise ValueError("entities and relationships must be arrays")

    entities: list[Entity] = []
    for index, item in enumerate(data["entities"]):
        if not isinstance(item, Mapping):
            raise ValueError(f"entities[{index}] must be an object")
        for key in ("id", "type", "name", "addresses"):
            if key not in item:
                raise ValueError(f"entities[{index}] is missing {key}")
        if not all(_non_empty_string(item[key]) for key in ("id", "type", "name")):
            raise ValueError(f"entities[{index}] id, type, and name must be non-empty strings")
        if not isinstance(item["addresses"], list):
            raise ValueError(f"entities[{index}].addresses must be an array")
        addresses: list[SemanticAddress] = []
        for address_index, raw in enumerate(item["addresses"]):
            if not isinstance(raw, Mapping):
                raise ValueError(f"entities[{index}].addresses[{address_index}] must be an object")
            for key in ("x_layer_id", "y_module_id", "z_depth", "valid_from"):
                if key not in raw:
                    raise ValueError(f"entities[{index}].addresses[{address_index}] is missing {key}")
            addresses.append(SemanticAddress(
                raw["x_layer_id"], raw["y_module_id"], raw["z_depth"],
                raw["valid_from"], raw.get("valid_to"),
            ))
        metadata = item.get("metadata", {})
        if not isinstance(metadata, Mapping):
            raise ValueError(f"entities[{index}].metadata must be an object")
        entities.append(Entity(item["id"], item["type"], item["name"], tuple(addresses), dict(metadata)))

    relationships: list[Relationship] = []
    for index, item in enumerate(data["relationships"]):
        if not isinstance(item, Mapping):
            raise ValueError(f"relationships[{index}] must be an object")
        for key in ("source_id", "predicate", "target_id"):
            if key not in item:
                raise ValueError(f"relationships[{index}] is missing {key}")
        relationships.append(Relationship(
            item["source_id"], item["predicate"], item["target_id"],
            item.get("context"), item.get("status", "PROPOSED"),
        ))

    provenance = data.get("provenance", [])
    if not isinstance(provenance, list) or any(not isinstance(item, Mapping) for item in provenance):
        raise ValueError("provenance must be an array of objects")
    return SystemModel(
        data["model_id"], data["root_entity_id"], data["view_id"],
        tuple(entities), tuple(relationships), tuple(dict(item) for item in provenance),
    )
