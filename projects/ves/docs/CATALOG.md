# VES Card, Board, View and Deck Catalog

## Catalog responsibilities
The catalog describes reusable engineering card types, board types, card views and starter Decks. It does not create project entities. A catalog definition is a reusable template; a project Entity is an instantiated engineering object.

## Initial card type registry
14 card types are registered across hardware, software, data, interface, process, system, material and AI categories. Each type declares a stable type ID, label, category, description, default property fields and tags.

## Board type registry
12 board types: Freeform, Grid, Kanban, Mind Map, Flow, Architecture, Circuit, Assembly, Timeline, Matrix, Map and Game Board. Each declares layout semantics and whether typed relationships are supported.

## Card view registry
10 presentation modes: Mini, Compact, Standard, Technical, Visual, Game, Node, Exploded, Comparison and Document. Views are renderer metadata and do not create duplicate Entities.

## Starter Decks
- Universal Hardware
- Embedded Systems
- Software Architecture
- AI Systems
- Engineering Materials

A Deck contains references to card type IDs, not duplicated project entity records. Invalid references are reported by validate_deck.

## Implementation
src/ves_catalog.py exposes immutable definitions, DEFAULT_CATALOG, search_card_types and validate_deck. Catalog definitions are currently Python data; external JSON catalog loading and gallery UI are follow-up work.
