# VES Product Specification

**Version:** 0.1.0 · **Status:** Proposed baseline · **Date:** 2026-11-24

## Purpose
VES is a universal visual engineering workbench for describing, composing, inspecting, validating and documenting physical and digital systems. It is not merely a diagram editor: cards, boards and documents are projections of a shared semantic model.

## Approved decisions
| Dimension | Baseline |
|---|---|
| Scope | Universal: software, hardware, firmware, data, interfaces, processes, materials and systems |
| Visual | Hybrid: engineering precision + board-game composition + free canvas |
| Interaction | Cards, diagrams, graphs, forms and canvas |
| Platform | Web, Windows and Android |
| Priority | Full target architecture, phased implementation |
| Deployment | Local-first; cloud optional, never required for core editing |

## User outcomes
1. Model systems across hardware, software, firmware, data, interfaces and processes.
2. Represent each reusable engineering object once and show it through multiple views.
3. Compose systems by placing reusable cards on typed boards.
4. Connect entities with typed and inspectable relationships.
5. Capture requirements, constraints, decisions, tests and evidence.
6. Validate model consistency and export portable project data and documents.

## Functional requirements
- FR-001 Create and reopen a local project.
- FR-002 Create typed entities with stable IDs and properties.
- FR-003 Render an entity in multiple card views without duplicating the entity.
- FR-004 Place entity references on boards with independent layout coordinates.
- FR-005 Create typed relationships between existing entities.
- FR-006 Inspect and edit entity properties.
- FR-007 Validate dangling references, duplicate placements and unregistered types.
- FR-008 Import/export a versioned JSON project.
- FR-009 Preserve unknown extension properties where safe.
- FR-010 Record provenance and license metadata for external assets.

## Non-functional requirements
Local-first operation; renderer-independent model; stable IDs; deterministic findings; staged non-destructive import; portable data; accessible keyboard/touch alternatives; bounded resource use.

## Product boundaries
VES owns the universal model, visual workspace, card/deck/board/form systems and validation orchestration. Specialist engines remain adapters or external tools. VES v0.1 does not replace a complete SysML, UML, EDA, CAD, simulation or PLM suite.

## Out of scope for v0.1
Cloud sync, authentication, collaboration, plugin marketplace/sandbox, full SysML v2 parser/serializer, CAD kernel, PCB autorouting, HDL simulation, physics simulation and signed installers.

## First vertical slice
Create project → create Hardware, Software, Data and Interface entities → render cards → place on architecture board → connect → edit properties → validate → export → import → compare IDs, properties and relationships.
