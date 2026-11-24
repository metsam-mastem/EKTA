# ADR-0001: Semantic rather than Cartesian coordinate semantics

- **Status:** PROPOSED
- **Date:** 2026-11-24
- **Decision owner:** EKTA project owner
- **Scope:** UMSF 0.1

## Context

The originating sketch proposes X for layers, Y for modules, Z for depth/breadth/dimensions, and time as an additional dimension. EKTA already has independent Territory, Domain, Layer, and Knowledge Type taxonomies, plus a typed relationship graph. Treating every concept as a geometric axis would conflate classification, decomposition, scope, and graph topology.

## Decision

Adopt a semantic address `(X, Y, Z, T)` with these meanings:

- X = architectural layer ID from EKTA's layer registry.
- Y = stable functional module/subsystem identity; not an engineering domain.
- Z = non-negative, view-relative decomposition depth.
- T = temporal validity; record time and revision are tracked separately.

Keep relationships as a typed graph, and keep scope, breadth, scale, viewpoint, context, and metadata as explicit qualifiers.

## Consequences

Positive:
- Preserves compatibility with EKTA taxonomies and graph.
- Supports cross-layer modules and multiple views.
- Avoids false metric interpretation of categorical values.
- Separates structural decomposition from scope and coverage.
- Allows temporal assertions without making version history a coordinate-derived fact.

Trade-offs:
- Requires explicit module IDs and declared roots/views.
- A single entity may have multiple addresses.
- Depth is view-relative and cannot be treated as a global entity property.
- Graph and coordinate consistency need semantic validation beyond JSON Schema.

## Rejected alternatives

1. **X=layer, Y=domain, Z=all depth/breadth/scope:** rejected because domain is a subject classification, not necessarily a module instance, and scope/breadth are not decomposition depth.
2. **R as a fifth coordinate:** rejected because relationships are edges among entities, not a scalar/axis value.
3. **Treating XYZ as Euclidean space:** rejected because X and Y are categorical and Z is ordinal.
4. **One global hierarchy:** rejected because cross-cutting entities and multiple viewpoints can have multiple valid decompositions.

## Evidence and references

- Existing EKTA `docs/KNOWLEDGE_ARCHITECTURE.md`: domains, layers, and knowledge types are independent classification axes; concepts can have multiple tags.
- Existing EKTA `taxonomy/layers.yml`: canonical architectural layer identifiers.
- Existing EKTA `taxonomy/relations.yml`: controlled graph predicate vocabulary.
- ISO/IEC/IEEE 42010:2022: architecture descriptions support viewpoints and model kinds and distinguish an architecture from its description.
- W3C RDF 1.1: graph statements are subject-predicate-object triples.
- W3C OWL 2: formal vocabularies can define classes, properties, individuals, and data values.
- W3C PROV-O: provenance can represent entities, activities, agents, and generation/usage relations.

## Validation

This decision remains PROPOSED until reviewed. It becomes IMPLEMENTED only when the schema and validation code are committed; VALIDATED only after repository tests and CI pass.
