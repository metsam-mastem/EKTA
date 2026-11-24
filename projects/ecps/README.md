# ECPS — Engineering Coordinate & Projection System

**Version:** 0.1.0 · **Status:** PROPOSED / integration prototype  
**Host:** [EKTA](https://github.com/metsam-mastem/EKTA)

ECPS is the cross-workstream architecture for coordinating engineering coordinate semantics and synchronized projections across existing EKTA projects. It is **not** a second semantic model, mathematical engine, visual language, or workbench.

## Architectural decision

EKTA already has four complementary draft workstreams:

- **UMSF** — semantic system addresses, typed relationships, view-relative decomposition and temporal validity.
- **MUA** — mathematical objects and abstract/geometric coordinate-frame contracts.
- **VEL** — visual engineering language: nodes, ports, typed connections and visual grammar.
- **VES** — interactive workbench: entities, relationships, boards and board-local placements.

ECPS connects these systems through a renderer-neutral projection manifest. Each subsystem remains authoritative for its own model. ECPS stores references and projection rules, not duplicated engineering entities.

## Critical coordinate distinction

| Coordinate kind | Authority | Meaning |
|---|---|---|
| `semantic-address` | UMSF | X=layer ID, Y=module ID, Z=view-relative depth, T=validity |
| `geometric-frame` | MUA | Mathematical frame, axes, origin, basis and units policy |
| `board-layout` | VES | Board-local placement for arranging a workbench view |
| `diagram-topology` | VEL | Nodes, ports and typed connections |
| `relationship-graph` | UMSF | Typed semantic relations independent of spatial adjacency |
| `temporal-validity` | UMSF | Valid-time and revision assertions |
| `mathematical-representation` | MUA | Symbolic, tabular, 2D/3D, graph and procedural representations |

A VES board position or VEL visual layout MUST NOT be interpreted as a physical measurement. UMSF semantic X/Y/Z MUST NOT be used as Cartesian x/y/z. Relationships are explicit graph edges, not inferred from coordinate proximity.

## Current implementation (0.1.0)

- Versioned projection-manifest JSON Schema.
- Python validator for source-model references, coordinate-space references, authority alignment and view/coordinate-kind compatibility.
- Deterministic renderer-neutral projection-plan compiler.
- Federated example referencing the four draft workstreams by exact commit.
- Unit tests and validation CLI.

Not implemented: import/export adapters, actual rendering, coordinate transformation, model synchronization, CAD/PCB integration, simulation, or editing source models. The projection compiler currently produces a plan only.

## Run from EKTA root

```bash
python tools/validate_ecps.py
python -m unittest discover -s tests -p 'test_ecps.py' -v
```

## Documents

- [Core specification](SPECIFICATION.md)
- [Architecture and federation decision](ARCHITECTURE.md)
- [Workstream integration matrix](INTEGRATION_MATRIX.md)
- [Research register](RESEARCH_REGISTER.md)
- [Projection manifest example](examples/integrated-engineering-view.json)
- [JSON Schema](../../schemas/ecps-projection.schema.json)
- [Python contract core](src/ecps/)

## Governance

The four referenced workstreams are draft PRs at the recorded audit snapshot. ECPS does not merge, rewrite or supersede them. Reconcile contracts after their review/merge. All adapters require explicit loss reports and conformance tests. No third-party code is copied or vendored. EKTA's existing license status is unchanged.
