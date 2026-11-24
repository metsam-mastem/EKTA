# ECPS Architecture — Federated Engineering Projection

## 1. Architecture decision

**Decision:** use a federated model architecture with source-specific authority and a shared projection manifest. Do not create a competing universal entity store in ECPS 0.1.

This is a deliberate correction to the earlier single-model proposal. The EKTA workstreams already have distinct, useful contracts. Forcing them into one schema would erase important differences between semantic architecture, mathematical geometry, visual topology and workbench layout.

## 2. Logical architecture

```text
                  EKTA Knowledge / Governance
                             |
                    ECPS Projection Manifest
                             |
       +---------------------+---------------------+
       |                     |                     |
      UMSF                  MUA                   VEL / VES
 semantic system       mathematics &          visual grammar /
 model + graph         coordinate frames     interactive boards
       |                     |                     |
       +---------------------+---------------------+
                             |
                  Projection Plan Compiler
                             |
       +----------+----------+----------+----------+
       |          |          |          |          |
   Semantic    Geometry   Diagram    Board     Timeline /
   Architecture 3D/2D     Graph      Canvas    Matrix / Math
```

## 3. Authority boundaries

| Workstream | Authoritative data | ECPS consumes |
|---|---|---|
| UMSF | Entity identity, semantic addresses, graph relations, temporal assertions | Entity/relation references and semantic/temporal view definitions |
| MUA | Mathematical objects, coordinate frames, mathematical representations | Frame references, axes/unit metadata and representation references |
| VEL | Visual nodes, ports, channels, connections, groups and status | Visual model reference and topology projection definition |
| VES | Project entities, relationships, boards and placements | Board reference and view-state projection definition |

ECPS is not authoritative for the source data above. The manifest is authoritative only for its own cross-workstream projection declarations.

## 4. Four distinct position/relationship concepts

1. **Semantic address (UMSF):** where an entity belongs in a declared architectural view.
2. **Geometric coordinate (MUA):** where a mathematical/physical object lies in a declared coordinate frame.
3. **Board placement (VES):** where a card is arranged on a workbench board.
4. **Diagram topology (VEL):** how nodes, ports and typed connections are visually/structurally related.

These are not interchangeable. The same entity may have all four references, but conversion requires an explicit mapping with provenance and validation.

## 5. Runtime boundary

The 0.1 Python core is deliberately small:

- validate source-model references;
- validate coordinate-space references;
- validate view-kind compatibility;
- validate source authority alignment;
- compile a deterministic, renderer-neutral projection plan.

Rendering, graph layout, 3D geometry, symbolic computation, CAD/PCB operations and source-model editing remain in their owning subsystem or an external adapter.

## 6. Adapter architecture

Each adapter declares:

- source subsystem and schema version;
- supported fields/entities/relations;
- mapping table and identifier strategy;
- coordinate-space semantics;
- import/export direction;
- lossiness and unsupported constructs;
- deterministic fixtures and test tolerances;
- source commit and provenance.

Adapters must not fabricate ports, physical dimensions, units, semantic layers or relations. Unsupported data must be preserved as opaque metadata where safe or reported in a loss report.

## 7. Rendering and device strategy

- 2D and matrix views are the low-resource default.
- 3D rendering is lazy and optional.
- Renderer dependencies do not enter the semantic or mathematical core.
- Mobile/low-memory clients consume projection plans and may render simplified views.
- Desktop/web clients may attach specialist renderers through replaceable adapters.

## 8. Versioning and synchronization

A manifest pins source revisions. A projection is reproducible only against the exact source revision and adapter version. When a source changes, the projection is marked stale until revalidated. No silent refresh or overwrite is allowed.

## 9. Security

Source models and external adapter outputs are untrusted input. Validate before projection. Do not execute embedded expressions or arbitrary plugins. A projection plan contains references and metadata, not executable code or secrets.
