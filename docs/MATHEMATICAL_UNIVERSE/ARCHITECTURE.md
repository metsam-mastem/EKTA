# Mathematical Universe Architecture (MUA)

**Project:** EKTA  
**Status:** PROPOSED — foundation slice submitted for review  
**Version:** 0.1.0  
**Scope:** Universal mathematical representation and engineering workspace

## 1. Purpose

MUA defines a representation-independent architecture for mathematical knowledge and work. A mathematical entity is not reduced to a formula image or chart. It has identity, semantics, structure, behavior, typed relations, representations, constraints, and provenance.

MUA is an EKTA subsystem, not a separate canonical project or competing knowledge repository.

## 2. Four conceptual worlds

1. **Ontological world:** mathematical kinds, definitions, identity, classification, and conceptual relations.
2. **Spatial/physical world:** geometric structures, coordinate frames, dimensions, transformations, and time-dependent models.
3. **Intelligent world:** retrieval, interpretation, symbolic/numerical execution, proof checking, and evidence-backed reasoning.
4. **Workbench world:** authoring, inspection, composition, simulation, validation, versioning, and export.

These are synchronized views over shared canonical entities, not four independent data stores.

## 3. Core invariants

- One stable identity per canonical entity; IDs are never recycled.
- Semantics are independent of visual appearance and renderer.
- One entity may have multiple simultaneous representations.
- Coordinate frames are mathematical objects, not UI pixel coordinates.
- Knowledge-graph placement, mathematical coordinates, and workspace layout are distinct spatial systems.
- Relations are typed and directed unless explicitly defined otherwise.
- A renderer must not silently alter mathematical meaning.
- AI suggestions are not proofs; computation and proof status require explicit evidence.
- Unknown, approximate, and unverified properties remain explicitly marked.
- Foundation records are versioned and Git-native; no external database is required.

## 4. Universal Mathematical Object (UMO)

The initial contract contains:

| Area | Responsibility |
|---|---|
| schema_version | Contract compatibility |
| id, kind, identity | Stable identity and type |
| revision, status | Lifecycle and maturity |
| semantics | Definition, scope, notation, assumptions |
| structure | Components, dimensions, domains, coordinate-frame references |
| behavior | Operations, laws, state and I/O contracts |
| relations | Typed links to other UMO records |
| representations | Symbolic, textual, tabular, 2D, 3D, spatial, graph, procedural, multimodal |
| constraints | Preconditions, invariants, bounds, domain restrictions |
| provenance | Sources, dates, confidence |
| extensions | Namespaced future capabilities |

The JSON Schema is a structural contract. It does not prove mathematical truth or consistency.

## 5. Coordinate-frame model

Coordinate frames specify dimension, coordinate kind, ordered axes, origin, optional basis and handedness, units policy, and optional time-axis designation.

Do not assume X/Y/Z always mean physical space. Axis semantics must be declared. Parameters, time, frequency, phase, or other independent variables may be represented only when the model explicitly defines them.

Coordinate transformation is not implemented in this foundation slice. It requires explicit source/target frames, transformation semantics, validity conditions, and numerical tolerances.

## 6. Visual grammar

Visual grammar maps semantic roles to visual channels without making color the sole carrier of meaning.

Candidate channels:
- geometry: point, curve, surface, volume, cell, node, edge, field;
- topology: adjacency, containment, boundary, connectivity;
- direction: arrowheads, orientation, flow;
- magnitude: scale, thickness, opacity, or numeric labels;
- uncertainty: intervals, bands, error bars, or explicit uncertainty marks;
- state: shape, outline, pattern, and accessible textual label;
- dimension: 1D/2D/3D/higher-dimensional projection with disclosed information loss.

A visual profile is renderer metadata; it cannot redefine the mathematical object. Accessibility, monochrome readability, and consistent legend semantics are acceptance requirements.

## 7. Runtime boundaries

Separate responsibilities:
- ontology/taxonomy service;
- UMO registry;
- typed relation graph;
- symbolic computation adapter;
- numerical computation adapter;
- geometry adapter;
- proof adapter;
- notation/chart/2D/3D renderer adapters;
- workspace shell.

No engine is a mandatory dependency in version 0.1.0. Adapters must be replaceable and capability-declared.

## 8. Execution and trust model

A calculation result should carry engine name/version, input identity/revision, parameters, assumptions, precision/tolerance, output, and execution status. A proof result should carry checker identity/version and a reproducible proof artifact or reference. An AI explanation is labeled as explanation, not verified result.

Do not use a single boolean validity flag to conflate schema validity, mathematical truth, numerical stability, and proof verification.

## 9. Integration with EKTA

MUA follows EKTA governance, Git-native source of truth, schema-first validation, evidence/provenance rules, and CI workflow. Mathematical kinds must not be forced into EKTA engineering-domain or engineering-layer identifiers.

Future concept records should link to MUA entities through stable IDs and typed relations rather than duplicate definitions.

## 10. Delivery roadmap

| Stage | Deliverable | Exit condition |
|---|---|---|
| M0 | Architecture and contracts | Schema review and invariants agreed |
| M1 | UMO validation library | Deterministic unit tests |
| M2 | Coordinate and relation model | Dimensional and referential integrity tests |
| M3 | Visual grammar registry | Semantic encodings and accessibility rules |
| M4 | Symbolic/numerical adapters | Adapter contract and reproducible outputs |
| M5 | Geometry and projection adapters | Explicit transform contracts and tests |
| M6 | Workbench vertical slice | Create, inspect, render, version, export one entity |
| M7 | Engineering integrations | One verified cross-domain workflow |

## 11. Current implementation boundary

Included in the foundation slice: UMO and coordinate-frame JSON Schemas, dependency-free structural validation helpers, relation target checks, a quadratic-function example, and unit tests.

Not included: symbolic/numerical computation, theorem proving, coordinate transforms, rendering, visual editor, AI reasoning, or persistence beyond Git-native files.

CI evidence: the initial foundation commit (bc0a8eda507cb34894dc082b49c621b1dd0123bf) passed the repository GitHub Actions workflow, including documentation validation, unit/runtime tests, frontend validation, and knowledge-graph export (run 45303560150). Later schema/example test additions are being revalidated on the current pull-request head; consult PR #19 for the latest status.
