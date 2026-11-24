# EKTA Cross-Subsystem Integration Matrix

| Concern | Canonical owner | Consumes / references | Must not be confused with |
|---|---|---|---|
| Engineering territories, domains, layers, knowledge types | EKTA taxonomy | All subsystems | USDO facets or UMSF module slots |
| Cross-domain structural facets | USDO | EKTA IDs and registries | Replacement for EKTA taxonomy |
| Semantic system address X/Y/Z/T | UMSF | EKTA layer/domain/territory registries | Physical Cartesian coordinates or graph edges |
| Mathematical entity identity and representation | MUA / UMO | EKTA source and concept IDs; coordinate-frame references | Rendered formula image or UI position |
| Visual model nodes, ports, connectors, groups | VEL | EKTA stable IDs; optional MUA/USDO/UMSF references | Canonical knowledge definitions |
| Visual engineering product shell and board workflows | VES | VEL model interchange and EKTA references | VEL language itself or EKTA runtime dependency |
| Collaboration methods and organizational practice | Collaboration Atlas | EKTA taxonomy and source evidence | Runtime multi-user collaboration feature |
| Project document lifecycle and continuity | UPDS #23 (proposed) | EKTA project governance and records | Approved replacement for current EKTA governance |
| Engineering knowledge organization view | PR #22 (proposed) | Canonical EKTA territories and terminology | A replacement for the canonical taxonomy registries |
| External technical documentation | Source registry / GitHub Docs | EKTA source IDs and taxonomy crosswalk | Canonical concepts until reviewed |
| User-provided concept-series archive | Staging intake | Hash manifest, source metadata, schema validator | Canonical Encyclopedia before review; record 000008 currently collides with an already canonical Hardware Knowledge Atlas ID |
| Hardware Knowledge Atlas / GTC | GTC upstream + EKTA integration record | Pinned submodule commit and claim-level source provenance | Automatic ingestion or re-licensing of upstream content |

## Coordinate-system separation

| System | Coordinates / axes | Meaning | Valid operations |
|---|---|---|---|
| UMSF | X, Y, Z, T | Semantic address relative to a declared view | Addressing, view filtering, temporal validity; no Euclidean distance on categorical axes |
| MUA coordinate frame | Declared axes, origin, basis, units, handedness, optional time axis | Mathematical coordinate frame | Explicit transforms only when source/target frames and tolerances are defined |
| VEL/VES layout | Board coordinates and placements | Visual arrangement of model cards/nodes | Layout, routing, hit-testing, viewport operations |
| EKTA knowledge graph | Node identity and typed directed edges | Semantic relations | Traversal and graph queries; no spatial metric implied |

## Cross-integration contract

- Subsystems use their own schema version and namespaced paths.
- Stable EKTA IDs are referenced, not duplicated or redefined.
- External relation predicates map explicitly to EKTA relation IDs; no implicit predicate promotion.
- Unknown target IDs remain unresolved with a reason; validators must not invent targets.
- Derived visualizations carry source revision and generator version.
- Schema changes are reviewed before dependent subsystem changes merge.
- Canonical data remains Git-native and rebuildable.
