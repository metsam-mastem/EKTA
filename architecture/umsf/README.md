# UMSF — Universal Multidimensional System Framework

**Status:** PROPOSED / research-backed design baseline  
**Version:** 0.1.0  
**Parent project:** EKTA — Engineering Knowledge & Techniques Atlas  
**Canonical branch for this work:** `architecture/umsf-coordinate-framework-v0.1`

## Purpose

UMSF is a reusable semantic-coordinate and relationship framework for describing systems, their parts, architectural layers, functional modules, structural decomposition, temporal evolution, scope, context, and evidence.

UMSF is an EKTA subsystem, not a separate source of truth. Canonical knowledge remains Git-native. UMSF records and exports must use EKTA stable IDs, taxonomy registries, relation vocabulary, provenance conventions, and validation gates.

## Core model

UMSF deliberately separates four concerns:

1. **Semantic address** — a view-relative coordinate `(X, Y, Z, T)`.
2. **Entity identity** — stable ID and type, independent of its address.
3. **Relationship graph** — typed edges between entities; not another coordinate axis.
4. **Context and metadata** — scope, viewpoint, constraints, provenance, status, and other qualifiers.

### Coordinate semantics

| Symbol | Canonical meaning | Domain |
|---|---|---|
| X | Architectural layer | EKTA layer registry; multi-valued |
| Y | Functional module / subsystem slot | Stable module identity; not synonymous with domain |
| Z | Structural decomposition depth | Non-negative, relative to a declared root and view |
| T | Temporal validity / evolution | Time interval and recorded revision |

A coordinate is a **semantic address**, not a physical Cartesian measurement. Do not calculate Euclidean distance between categorical layer/module identifiers. Do not infer dependency, similarity, containment, or execution order from coordinate proximity.

### Important distinctions

- **Territory** is EKTA's portfolio/navigation grouping.
- **Domain** is a controlled engineering classification tag.
- **Layer** is an architectural classification axis.
- **Module** is an actual functional or structural system part with stable identity.
- **Depth** is the level of decomposition in a particular rooted view; it is not universal object complexity.
- **Scope** is the coverage boundary and is metadata, not the Z axis.
- **Breadth** is coverage across selected domains/modules, not depth.
- **Viewpoint / View** selects a concern-driven representation; it does not alter canonical identity.
- **Relationship** is a graph edge with its own predicate and provenance.
- **Time** distinguishes when a fact is valid from when EKTA recorded it.

## Fit with existing EKTA architecture

UMSF extends rather than replaces the existing EKTA classification model:

- Reuses `taxonomy/layers.yml` for X.
- Reuses `taxonomy/domains.yml` and `taxonomy/territories.yml` as classification/facet systems; neither is substituted for Y.
- Reuses `taxonomy/relations.yml` for graph predicates.
- Uses canonical EKTA IDs for entities and relation endpoints.
- Keeps module identity and containment in the entity/graph model.
- Exports derived views only; canonical records remain in Git.

## Model boundary

UMSF v0.1 is a data contract and a small pure-Python validation core. It does not yet implement a 3D renderer, database, editor, ontology reasoner, time-series engine, or write-enabled API.

## Directory map

- [MODEL_SPEC.md](MODEL_SPEC.md) — concepts, invariants, coordinate rules.
- [DATA_CONTRACT.md](DATA_CONTRACT.md) — JSON representation and examples.
- [RESEARCH_REGISTER.md](RESEARCH_REGISTER.md) — standards and open technical foundations.
- [ADR-0001-coordinate-semantics.md](ADR-0001-coordinate-semantics.md) — key architectural decision.
- [../../schemas/umsf.schema.json](../../schemas/umsf.schema.json) — JSON Schema.
- [../../runtime/ekta_runtime/umsf.py](../../runtime/ekta_runtime/umsf.py) — validation core and JSON-compatible import/export.
- [../../tests/test_umsf.py](../../tests/test_umsf.py) — unit tests, round-trip, provenance, and malformed-input regression coverage.

## Status discipline

PROPOSED means the design is recorded but not yet approved as a project-wide standard. IMPLEMENTED applies only to files/code present in the repository. VALIDATED requires the relevant tests and CI evidence. The v0.1 remote files must not be described as runtime-integrated until the import/API/build path is explicitly connected and tested.
