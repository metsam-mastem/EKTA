# VES UX and Interaction System

## Workspace shell
- Left navigation: projects, boards, gallery, decks, templates and search.
- Main work surface: board/canvas/diagram.
- Right inspector: selected entity, relationships, properties, provenance and validation.
- Top command bar: save, undo/redo, view switch, validate, import/export and search.
- Mobile: bottom navigation, full-screen inspector, touch-safe cards and simplified tools.

## Interaction modes
Selection, drag/drop, connect, resize, group, align, zoom/pan, keyboard navigation, touch gestures, context actions and form editing. Critical drag actions should have keyboard/menu alternatives.

## Card views
Mini, Compact, Standard, Technical, Visual, Game, Node, Exploded, Comparison and Document. Each view renders the same entity ID; hiding fields must not mutate or discard them.

## Board types
Freeform, Grid, Kanban, Mind Map, Flow, Architecture, Circuit, Assembly, Timeline, Matrix, Map and Game Board. Each board declares allowed node/edge semantics, layout constraints and supported interactions.

## Gallery and Deck
Gallery is a searchable catalog of reusable entities, templates, visual assets and Decks. Deck is a curated collection of references and optional ordering/rules. Board is a working composition. Reuse must not duplicate canonical identity unless the user explicitly clones.

## Inspector and accessibility
Inspector exposes type, identity, properties, ports, relationships, requirements, evidence, provenance, version and status. Unknown fields remain visible in advanced view. Color is never the sole carrier of meaning. Keyboard focus, visible focus states, sufficient contrast, reduced motion and non-color status encoding are production requirements.

## Responsive behavior
Desktop: multi-panel workspace. Tablet: collapsible inspector and touch canvas. Phone: browse/edit cards and forms, inspect relationships and lightweight board arrangement; dense diagram editing may be deferred to larger screens.
