# VES System Architecture

**Status:** Proposed baseline · **Version:** 0.1.0

## Architectural invariant
The canonical model is the source of truth. A card is a view of an entity; a placement is a board-specific reference; a diagram is a projection of entities and relationships. Rendering state is never a second canonical data store.

## Logical layers
1. Platform runtime — browser, desktop shell, Android shell and local filesystem.
2. Integration — importers, exporters, external-tool adapters and plugin contracts.
3. Storage/versioning — SQLite local store, versioned JSON interchange, asset files and optional Git snapshots.
4. Engineering services — validation, traceability, compatibility, search and provenance.
5. Domain engines — systems, software, hardware, electronics, data, network, process and materials.
6. Language adapters — SysML v2/KerML, UML, C4, BPMN, ERD, OpenAPI, EDA/HDL.
7. Unified model — project, entity, relationship, port, constraint, requirement and evidence.
8. Interaction — selection, drag/drop, connect, zoom/pan, keyboard, touch and inspector.
9. Experience — workspace, boards, cards, decks, gallery, forms and reports.

## v0.1 implementation
The domain core is a Python standard-library module. SQLite provides initial local persistence with transactional writes and optional optimistic revision checks. The visual proof-of-concept is a dependency-free browser app using localStorage for its demo state. A later production client may adopt React + TypeScript, XYFlow, a schema-driven form engine and desktop/mobile shells. These are replaceable adapters, not domain dependencies.

## Integration boundaries
- EKTA integration is knowledge registration and taxonomy crosswalk, not a runtime dependency.
- SysON is a candidate SysML adapter; no conformance claim before fixtures pass.
- BPMN.io, KiCad and specialist tools remain external processes/file adapters until license, interface and data-loss behavior are verified.
- Third-party plugins receive capability-scoped interfaces; arbitrary plugin code is untrusted.

## Quality attributes
Portability, offline operation, stable identifiers, deterministic validation, reversible changes, format transparency, modular adapters, accessibility and bounded resource use.
