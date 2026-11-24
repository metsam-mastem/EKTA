# ECPS Integration Matrix

Snapshot date: 2026-11-24. All four upstream workstreams below were observed as open draft PRs; this document does not imply they have merged.

## 1. Workstream inventory

| Workstream | Draft PR | Branch | Contract / code | ECPS role |
|---|---|---|---|---|
| UMSF | [#11](https://github.com/metsam-mastem/EKTA/pull/11) | `architecture/umsf-coordinate-framework-v0.1` | `architecture/umsf/`, `schemas/umsf.schema.json`, `runtime/ekta_runtime/umsf.py` | Semantic addresses, typed graph, view-relative depth, temporal validity |
| VEL | [#10](https://github.com/metsam-mastem/EKTA/pull/10) | `project/vel-language-v0.1` | `projects/vel/`, `schemas/vel-model.schema.json`, `runtime/ekta_runtime/vel.py` | Visual node/port/connection grammar and diagram topology |
| MUA | [#19](https://github.com/metsam-mastem/EKTA/pull/19) | `workbench/mua-foundation-0.1.0` | `docs/MATHEMATICAL_UNIVERSE/`, `schemas/coordinate-frame.schema.json`, `schemas/mathematical-object.schema.json`, `runtime/ekta_runtime/mathematics.py` | Mathematical objects, coordinate frames and mathematical representations |
| VES | [#20](https://github.com/metsam-mastem/EKTA/pull/20) | `project/ves-foundation-v0.1` | `projects/ves/`, `projects/ves/schemas/project.schema.json`, `projects/ves/src/ves_core.py` | Interactive workbench, project entities, relationships, boards and placements |

## 2. Coordinate and identity crosswalk

| Concern | Canonical owner | Identifier / representation | ECPS rule |
|---|---|---|---|
| Engineering entity identity | UMSF / VES according to source record | UMSF entity ID; VES entity ID | Preserve source namespace; use explicit cross-reference when linking |
| Architectural layer | UMSF + EKTA layer registry | `x_layer_id` | Never convert to numeric x-position |
| Functional module | UMSF | `y_module_id` | Stable module identity, not a domain label |
| Decomposition depth | UMSF | `z_depth` | Ordinal and view-relative, not physical z |
| Validity time | UMSF | `valid_from`, `valid_to` and revision | Temporal semantics, not automatically a geometric axis |
| Geometric frame | MUA | `id`, `dimension`, `coordinate_kind`, `axes`, `origin`, optional basis/units | Physical/mathematical frame metadata only |
| Mathematical object | MUA | UMO ID, semantics, representations, structure/behavior | ECPS references it; MUA owns mathematical semantics |
| Visual node and ports | VEL | node ID, kind, label, ports | No entity identity from screen position or label |
| Visual connection | VEL | connection ID, channel kind, source/target node+port | Requires explicit ports and typed connection |
| Workbench board | VES | board ID/type | Board is a view container |
| Board placement | VES | entity ID, board-local x/y, card view | View-state only; never physical geometry |

## 3. Projection profiles

| Projection | Source | Coordinate kind | Output responsibility |
|---|---|---|---|
| Semantic architecture | UMSF | semantic-address | Layer/module/depth/time-aware architectural view |
| Dependency matrix | UMSF | relationship-graph | Adjacency/dependency matrix using explicit relations |
| Timeline | UMSF | temporal-validity | Valid-time/revision view |
| Mathematical plot | MUA | mathematical-representation | Renderer selected for object representation and declared frame |
| Physical 2D/3D | MUA | geometric-frame | Geometry renderer using declared frame/units/tolerances |
| Visual engineering diagram | VEL | diagram-topology | Cards/nodes, ports, channels and typed connections |
| Workbench board | VES | board-layout | Interactive board arrangement and inspector view |

## 4. Draft PR coordination and base alignment

At the 2026-11-24 snapshot:

- EKTA `main` was at `7ea271e00ef2cb010c17bdaa553e1f27645f12ca`.
- VEL PR #10 and UMSF PR #11 were based on `c5868113dd3044837d840b29a588fd1a59b70e90`, the parent of the current main snapshot. They should be reviewed/rebased against current main before merge.
- MUA PR #19 and VES PR #20 were based on the current main snapshot `7ea271e00ef2cb010c17bdaa553e1f27645f12ca`.
- The four PRs were open drafts. Their source branches remain independent.

ECPS must not rewrite, merge, close or force-update these branches. Once the workstream PRs are reviewed and merged, update this crosswalk against their canonical main-branch contracts and rerun conformance fixtures.

## 5. Integration sequence

1. Review and stabilize UMSF semantic-address and relationship contracts.
2. Review and stabilize MUA coordinate-frame and mathematical-object contracts.
3. Review and stabilize VEL node/port/connection visual grammar.
4. Review and stabilize VES entity/relationship/board/placement boundaries.
5. Implement read-only adapters and fixture-based import tests.
6. Add cross-model identity links and loss reports.
7. Add synchronized projections and stale-source detection.
8. Permit explicit source edits only through owner-specific APIs with evidence.

## 6. Known gaps

- No cross-workstream entity identity registry is implemented.
- No VEL-to-UMSF relation/port mapping is implemented.
- No MUA geometric frame transform graph is implemented by ECPS.
- No VES-to-physical-geometry mapping is permitted by default.
- No renderer is connected to the manifest compiler.
- No adapter round-trip compatibility is claimed.
