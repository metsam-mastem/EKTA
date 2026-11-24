"""Curated, renderer-independent card, board, view and Deck catalogs."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class CardTypeDefinition:
    type_id: str
    label: str
    category: str
    description: str
    default_fields: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()


@dataclass(frozen=True)
class BoardTypeDefinition:
    type_id: str
    label: str
    layout: str
    supports_relationships: bool
    description: str


@dataclass(frozen=True)
class CardViewDefinition:
    view_id: str
    label: str
    density: str
    purpose: str


@dataclass(frozen=True)
class DeckDefinition:
    deck_id: str
    name: str
    card_type_ids: tuple[str, ...]
    description: str = ""
    version: str = "1.0.0"


@dataclass(frozen=True)
class VesCatalog:
    card_types: tuple[CardTypeDefinition, ...]
    board_types: tuple[BoardTypeDefinition, ...]
    card_views: tuple[CardViewDefinition, ...]
    decks: tuple[DeckDefinition, ...]


CARD_TYPES = (
    CardTypeDefinition("hardware.mcu", "Microcontroller", "hardware", "Embedded programmable controller", ("architecture", "clock_mhz", "voltage_v", "interfaces"), ("compute", "embedded")),
    CardTypeDefinition("hardware.processor", "Processor", "hardware", "General-purpose processing unit", ("architecture", "cores", "frequency_mhz", "power_w"), ("compute",)),
    CardTypeDefinition("hardware.sensor", "Sensor", "hardware", "Physical measurement component", ("measured_quantity", "range", "accuracy", "interface"), ("input",)),
    CardTypeDefinition("hardware.actuator", "Actuator", "hardware", "Physical output or motion component", ("output_type", "voltage_v", "current_a"), ("output",)),
    CardTypeDefinition("software.application", "Application", "software", "User-facing or system application", ("language", "runtime", "version"), ("software",)),
    CardTypeDefinition("software.service", "Service", "software", "Deployable software service", ("protocol", "endpoint", "availability"), ("software", "service")),
    CardTypeDefinition("software.firmware", "Firmware", "software", "Software executing on embedded hardware", ("target", "language", "version"), ("embedded",)),
    CardTypeDefinition("data.database", "Database", "data", "Structured data persistence component", ("engine", "schema", "storage_gb"), ("data",)),
    CardTypeDefinition("interface.api", "API", "interface", "Programmatic interface contract", ("style", "version", "auth"), ("integration",)),
    CardTypeDefinition("interface.protocol", "Protocol", "interface", "Communication protocol or bus", ("standard", "transport", "data_rate"), ("communication",)),
    CardTypeDefinition("process.workflow", "Workflow", "process", "Ordered or event-driven process", ("trigger", "steps", "owner"), ("process",)),
    CardTypeDefinition("system.module", "System Module", "system", "Composable subsystem or module", ("responsibility", "boundary", "interfaces"), ("architecture",)),
    CardTypeDefinition("material.material", "Material", "material", "Physical material with engineering properties", ("composition", "density", "thermal_properties"), ("physical",)),
    CardTypeDefinition("ai.model", "AI Model", "ai", "Machine learning model or inference endpoint", ("family", "parameters", "runtime", "license"), ("intelligence",)),
)

BOARD_TYPES = (
    BoardTypeDefinition("freeform", "Freeform Canvas", "freeform", True, "Unconstrained spatial composition"),
    BoardTypeDefinition("grid", "Grid Board", "grid", True, "Aligned grid of engineering objects"),
    BoardTypeDefinition("kanban", "Kanban Board", "columns", False, "Work items organized by state"),
    BoardTypeDefinition("mindmap", "Mind Map", "radial", True, "Concepts organized around a central topic"),
    BoardTypeDefinition("flow", "Flow Board", "directed", True, "Directed process and control flow"),
    BoardTypeDefinition("architecture", "Architecture Board", "layered", True, "Systems and software architecture composition"),
    BoardTypeDefinition("circuit", "Circuit Board", "schematic", True, "Electronic schematic composition"),
    BoardTypeDefinition("assembly", "Assembly Board", "exploded", True, "Physical assembly and part relationships"),
    BoardTypeDefinition("timeline", "Timeline", "time", True, "Time-ordered events and milestones"),
    BoardTypeDefinition("matrix", "Matrix Board", "matrix", False, "Two-dimensional comparison or classification"),
    BoardTypeDefinition("map", "Map Board", "spatial", True, "Geographic or spatial engineering layout"),
    BoardTypeDefinition("game", "Game Board", "rules", True, "Rule-driven strategic composition"),
)

CARD_VIEWS = (
    CardViewDefinition("mini", "Mini", "minimal", "Dense overview"),
    CardViewDefinition("compact", "Compact", "compact", "Gallery and search results"),
    CardViewDefinition("standard", "Standard", "balanced", "General board work"),
    CardViewDefinition("technical", "Technical", "detailed", "Engineering specifications"),
    CardViewDefinition("visual", "Visual", "image-led", "Asset and material exploration"),
    CardViewDefinition("game", "Game", "collectible", "Board-game-like composition"),
    CardViewDefinition("node", "Node", "graph", "Relationship-centric view"),
    CardViewDefinition("exploded", "Exploded", "hierarchical", "Subcomponents and assembly"),
    CardViewDefinition("comparison", "Comparison", "tabular", "Side-by-side evaluation"),
    CardViewDefinition("document", "Document", "editorial", "Documentation and evidence"),
)

DECKS = (
    DeckDefinition("deck.hardware.core", "Universal Hardware", ("hardware.mcu", "hardware.processor", "hardware.sensor", "hardware.actuator"), "Core physical computing elements"),
    DeckDefinition("deck.embedded.systems", "Embedded Systems", ("hardware.mcu", "hardware.sensor", "hardware.actuator", "software.firmware", "interface.protocol"), "Embedded product building blocks"),
    DeckDefinition("deck.software.architecture", "Software Architecture", ("software.application", "software.service", "data.database", "interface.api"), "Application, service, data and API elements"),
    DeckDefinition("deck.ai.systems", "AI Systems", ("ai.model", "software.service", "data.database", "interface.api"), "Model and inference system elements"),
    DeckDefinition("deck.materials", "Engineering Materials", ("material.material", "hardware.actuator", "hardware.sensor"), "Materials and physical component references"),
)

DEFAULT_CATALOG = VesCatalog(CARD_TYPES, BOARD_TYPES, CARD_VIEWS, DECKS)


def search_card_types(catalog: VesCatalog, query: str = "", category: str | None = None) -> list[CardTypeDefinition]:
    needle = query.casefold().strip()
    results = []
    for item in catalog.card_types:
        if category and item.category.casefold() != category.casefold():
            continue
        haystack = " ".join((item.type_id, item.label, item.description, *item.tags)).casefold()
        if needle and needle not in haystack:
            continue
        results.append(item)
    return sorted(results, key=lambda item: (item.category, item.label.casefold()))


def validate_deck(catalog: VesCatalog, deck: DeckDefinition) -> list[str]:
    known = {item.type_id for item in catalog.card_types}
    return [type_id for type_id in deck.card_type_ids if type_id not in known]
