# ECPS Projection Contract 0.1.0

**Status:** PROPOSED  
**Specification ID:** ECPS-SPEC-PROJECTION-0001  
**Date:** 2026-11-24

## 1. Purpose and non-goals

ECPS defines how independent EKTA engineering models are referenced and projected into coordinated views. It does not replace their domain contracts:

- UMSF owns semantic system addresses and graph semantics.
- MUA owns mathematical objects and coordinate-frame records.
- VEL owns visual engineering nodes, ports, connections and visual grammar.
- VES owns workbench projects, entities, relationships, boards and board-local placements.

ECPS 0.1 does not define a universal canonical engineering entity schema. It defines a federation manifest and view contract. A future unified model may be evaluated only if it preserves each source authority and provenance.

## 2. Canonical projection manifest

The manifest is a versioned JSON document with:

- `sourceModels`: stable local references to authoritative source artifacts and exact source revisions;
- `coordinateSpaces`: named coordinate/representation spaces with an explicit authority;
- `projections`: view declarations linking one source model to one compatible coordinate-space kind;
- `metadata`: provenance and status.

The structural contract is `schemas/ecps-projection.schema.json`. Cross-record validation is performed by `projects/ecps/src/ecps/contracts.py`.

## 3. Coordinate-space registry

| Kind | Owner | Semantics | Forbidden inference |
|---|---|---|---|
| `semantic-address` | UMSF | Layer ID, module ID, view-relative depth and validity | No Euclidean distance or physical placement |
| `geometric-frame` | MUA | Coordinate kind, axes, origin, basis, handedness and units policy | No assumption that a frame is a UI board |
| `board-layout` | VES | Board-local x/y placement and card view | No physical dimensions or mechanical coordinates |
| `diagram-topology` | VEL | Nodes, ports, channels and typed connections | No assumption that visual proximity creates a relation |
| `relationship-graph` | UMSF | Typed subject-predicate-object relations | No coordinate-axis encoding of edges |
| `temporal-validity` | UMSF | Valid time, record time and revision references | No automatic treatment as a spatial axis |
| `mathematical-representation` | MUA | Mathematical object representations and coordinate-aware structures | No claim that notation alone is executable semantics |

## 4. View compatibility

The 0.1 profile defines these required pairings:

| View type | Required coordinate-space kind | Source authority |
|---|---|---|
| `semantic-architecture` | `semantic-address` | UMSF |
| `geometry-3d` | `geometric-frame` | MUA |
| `workbench-board` | `board-layout` | VES |
| `visual-diagram` | `diagram-topology` | VEL |
| `dependency-matrix` | `relationship-graph` | UMSF |
| `timeline` | `temporal-validity` | UMSF |
| `mathematical-plot` | `mathematical-representation` | MUA |

A projection is invalid if its source model is missing, its coordinate space is missing, its view type is unsupported, its coordinate kind does not match the view, or the coordinate-space authority differs from the source system.

## 5. Identity and relations

1. Source entity IDs remain owned by their source model.
2. ECPS manifest IDs are local references, not replacements for source IDs.
3. Cross-model links must record both source-model reference and source entity ID.
4. A projection must preserve identity; it must not create a new engineering identity from a label or screen position.
5. Visual links, graph edges and physical connections are distinct typed relations. An adapter must not infer one from another.
6. A projection manifest references source revisions by immutable commit SHA where repository-backed.

## 6. Mutation policy

- `read-only`: the view cannot modify source records.
- `view-state-only`: edits affect only view state (e.g. VES board placements), not physical or semantic source data.
- `explicit-model-edit`: source-model changes require an explicit source-specific operation, validation and evidence. This policy is reserved; the 0.1 compiler does not execute edits.

## 7. Projection-plan contract

`compile_projection_plan(manifest, projection_id)` returns a deterministic renderer-neutral plan containing manifest/projection IDs, source-model identity/revision, coordinate-space identity/kind/authority, mutation policy, and renderer-neutral/read-only flags. It does not load, rewrite or render source models.

## 8. Validation levels

- Structural: JSON Schema Draft 2020-12.
- Referential: unique manifest/source/space/projection IDs and valid local references.
- Semantic: view-to-coordinate-kind compatibility and source-authority alignment.
- Adapter conformance (future): import/export fixtures, round-trip checks, precision/tolerance checks and explicit loss reports.
- Engineering validity: remains the responsibility of the authoritative domain subsystem and its evidence/test process.

## 9. Compatibility

Manifest schema version is independent of source model versions. Each source model records its own exact revision. A source schema upgrade must be handled by an adapter profile or explicit migration; ECPS must not silently coerce incompatible data.

## 10. Open decisions

- Cross-model stable identity and alias registry.
- Whether one projection may combine multiple source models and how conflicts are resolved.
- Geometric frame composition and transform-direction contract (MUA-owned).
- Typed unit code profile (UCUM/SI evaluation).
- Port-to-interface and relation-to-connection mapping (VEL/UMSF).
- Temporal event/valid-time projection policy.
- Cache invalidation and model-revision synchronization.
- Incremental projection and large-model performance.
