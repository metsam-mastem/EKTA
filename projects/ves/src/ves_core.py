"""Canonical renderer-independent VES domain model and service."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


def _id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:12]}"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Entity:
    id: str
    type: str
    name: str
    properties: dict[str, Any] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    status: str = "draft"
    version: int = 1
    created_at: str = field(default_factory=_now)
    updated_at: str = field(default_factory=_now)

    @classmethod
    def create(cls, entity_type: str, name: str, properties=None, tags=None):
        if not entity_type.strip() or not name.strip():
            raise ValueError("entity type and name are required")
        return cls(_id("ent"), entity_type.strip(), name.strip(), properties or {}, tags or [])


@dataclass
class Relationship:
    id: str
    source_id: str
    target_id: str
    type: str
    properties: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(cls, source_id, target_id, relation_type, properties=None):
        if source_id == target_id:
            raise ValueError("self relationships are not allowed in VES v0.1")
        if not relation_type.strip():
            raise ValueError("relationship type is required")
        return cls(_id("rel"), source_id, target_id, relation_type.strip(), properties or {})


@dataclass
class Placement:
    entity_id: str
    x: float = 0
    y: float = 0
    card_view: str = "standard"


@dataclass
class Board:
    id: str
    name: str
    board_type: str = "architecture"
    placements: list[Placement] = field(default_factory=list)

    @classmethod
    def create(cls, name, board_type="architecture"):
        if not name.strip():
            raise ValueError("board name is required")
        return cls(_id("brd"), name.strip(), board_type)


@dataclass
class Project:
    id: str
    name: str
    schema_version: str = "0.1.0"
    entities: dict[str, Entity] = field(default_factory=dict)
    relationships: dict[str, Relationship] = field(default_factory=dict)
    boards: dict[str, Board] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(cls, name):
        if not name.strip():
            raise ValueError("project name is required")
        return cls(_id("prj"), name.strip())

    def to_dict(self):
        return {
            "schema_version": self.schema_version,
            "project": {"id": self.id, "name": self.name, "metadata": self.metadata},
            "entities": [asdict(v) for v in self.entities.values()],
            "relationships": [asdict(v) for v in self.relationships.values()],
            "boards": [{"id": b.id, "name": b.name, "board_type": b.board_type,
                        "placements": [asdict(p) for p in b.placements} for b in self.boards.values()],
        }

    @classmethod
    def from_dict(cls, data):
        if data.get("schema_version") != "0.1.0":
            raise ValueError("unsupported VES schema_version")
        raw = data.get("project") or {}
        project = cls(raw["id"], raw["name"], data["schema_version"], metadata=raw.get("metadata", {}))
        for item in data.get("entities", []):
            entity = Entity(**item)
            if entity.id in project.entities:
                raise ValueError(f"duplicate entity id: {entity.id}")
            project.entities[entity.id] = entity
        for item in data.get("relationships", []):
            relation = Relationship(**item)
            if relation.id in project.relationships:
                raise ValueError(f"duplicate relationship id: {relation.id}")
            project.relationships[relation.id] = relation
        for item in data.get("boards", []):
            board = Board(item["id"], item["name"], item.get("board_type", "architecture"),
                          [Placement(**p) for p in item.get("placements", [])])
            if board.id in project.boards:
                raise ValueError(f"duplicate board id: {board.id}")
            project.boards[board.id] = board
        return project


ALLOWED_PREFIXES = ("hardware.", "software.", "data.", "interface.", "process.",
                    "requirement.", "test.", "material.", "system.", "network.", "ai.")
ALLOWED_RELATIONS = {"contains", "part_of", "connects_to", "depends_on", "implements",
                     "satisfies", "verifies", "consumes", "produces", "communicates_with",
                     "compatible_with", "conflicts_with", "derived_from"}


@dataclass
class Finding:
    code: str
    severity: str
    message: str
    subject_id: str | None = None

    def to_dict(self):
        return asdict(self)


def validate_project(project: Project) -> list[Finding]:
    findings = []
    for entity in project.entities.values():
        if not entity.name.strip():
            findings.append(Finding("VES-ENTITY-001", "error", "Entity name is empty", entity.id))
        if not entity.type.startswith(ALLOWED_PREFIXES):
            findings.append(Finding("VES-ENTITY-002", "warning", f"Unregistered entity type: {entity.type}", entity.id))
    for relation in project.relationships.values():
        if relation.source_id not in project.entities:
            findings.append(Finding("VES-REL-001", "error", "Relationship source does not exist", relation.id))
        if relation.target_id not in project.entities:
            findings.append(Finding("VES-REL-002", "error", "Relationship target does not exist", relation.id))
        if relation.type not in ALLOWED_RELATIONS:
            findings.append(Finding("VES-REL-003", "warning", f"Unregistered relationship type: {relation.type}", relation.id))
    for board in project.boards.values():
        seen = set()
        for placement in board.placements:
            if placement.entity_id not in project.entities:
                findings.append(Finding("VES-BOARD-001", "error", "Board placement references a missing entity", board.id))
            if placement.entity_id in seen:
                findings.append(Finding("VES-BOARD-002", "warning", "Entity placed more than once on board", board.id))
            seen.add(placement.entity_id)
    return findings


class VesService:
    def __init__(self, project: Project):
        self.project = project

    def add_entity(self, entity_type, name, properties=None, tags=None):
        entity = Entity.create(entity_type, name, properties, tags)
        self.project.entities[entity.id] = entity
        return entity

    def add_relationship(self, source_id, target_id, relation_type, properties=None):
        if source_id not in self.project.entities or target_id not in self.project.entities:
            raise KeyError("both relationship endpoints must exist")
        relation = Relationship.create(source_id, target_id, relation_type, properties)
        self.project.relationships[relation.id] = relation
        return relation

    def add_board(self, name, board_type="architecture"):
        board = Board.create(name, board_type)
        self.project.boards[board.id] = board
        return board

    def place_entity(self, board_id, entity_id, x=0, y=0, card_view="standard"):
        if board_id not in self.project.boards or entity_id not in self.project.entities:
            raise KeyError("board and entity must exist")
        board = self.project.boards[board_id]
        if any(p.entity_id == entity_id for p in board.placements):
            raise ValueError("entity is already placed on this board")
        placement = Placement(entity_id, float(x), float(y), card_view)
        board.placements.append(placement)
        return placement

    def validate(self):
        return validate_project(self.project)

    def export(self):
        return self.project.to_dict()

    @classmethod
    def import_data(cls, data):
        return cls(Project.from_dict(data))
