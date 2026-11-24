# VES ↔ EKTA Integration Contract

## Purpose
Register VES as an independent engineering project in EKTA while preserving the identity and lifecycle of both projects.

## Workspace mapping
| EKTA workspace | VES contribution |
|---|---|
| DISCOVERY | research notes, candidate OSS tools, standards evidence and source evaluation |
| ENCYCLOPEDIA | reviewed concepts for visual modeling, typed entities, boards, cards, views, relationships and validation; promotion requires EKTA review |
| DECISION LAB | ADRs, technology selection, license review and architecture trade-offs |
| EXECUTION LAB | VES source, schemas, tests, MVP plan, implementation evidence and releases |

## Boundaries
- VES lives under projects/ves with its own version and schema lifecycle.
- EKTA runtime does not import VES runtime modules.
- VES may reference EKTA concept/taxonomy IDs only after checking canonical registries.
- VES predicates do not automatically become EKTA graph predicates.
- VES drafts are not automatically promoted into canonical Encyclopedia records.
- This integration is additive; no existing project, taxonomy or runtime file is removed or overwritten.

## Crosswalk policy
Use existing EKTA territories, domains, layers and knowledge types. VES spans systems engineering, software, hardware/electronics, data, architecture, process engineering, product design and documentation. Exact canonical IDs are to be reconciled against current YAML registries in a dedicated follow-up; no IDs are invented here.

## Provenance
External source/asset records must retain URI, publisher, version/revision, retrieval date, license and checksum when applicable.

## Synchronization
Repository-level, review-driven exchange. VES may submit reviewed knowledge candidates through staged records/PRs. EKTA may provide curated references without becoming a hard runtime dependency.

## Current state
This integration adds a project namespace, registry and contract. It does not merge VES into EKTA main and does not claim a live runtime connector.
