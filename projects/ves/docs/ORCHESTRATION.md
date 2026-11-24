# VES Development Orchestration

**Orchestration baseline:** 0.1.0  
**Repository:** metsam-mastem/EKTA  
**Working branch:** project/ves-foundation-v0.1  
**Review:** PR #20 (draft; intentionally unmerged)

## Operating rule
One VES project namespace, one integration branch and one review path. Workstreams may be developed independently, but their artifacts must converge on the same versioned model and acceptance criteria. No direct writes to EKTA main and no merging unrelated EKTA project streams.

## Workstreams

| ID | Workstream | Scope | Dependency | Exit evidence |
|---|---|---|---|---|
| WS-A | Product and architecture | product brief, system boundaries, ADRs, layer model | none | reviewed spec and ADR |
| WS-B | Canonical model and schemas | Entity, Relationship, Board, Placement, Project, JSON contracts | WS-A | schema tests and round-trip tests |
| WS-C | Persistence and interchange | SQLite store, revisions, import/export and migration | WS-B | persistence and conflict tests |
| WS-D | Card, Deck and Form systems | type catalog, views, Decks, typed field validation | WS-B | catalog/form tests |
| WS-E | Visual workspace | Board, Inspector, Gallery, Deck views and touch behavior | WS-B, WS-D | browser interaction and responsive QA |
| WS-F | EKTA knowledge integration | taxonomy crosswalk, provenance and project registration | EKTA registries | crosswalk test and review |
| WS-G | Quality, security and release | CI, schema validation, license review, test evidence and packaging | all workstreams | green CI and release checklist |

## Parallelization strategy
- WS-A and WS-F can progress independently.
- WS-B is the shared contract and must stabilize before deep UI or persistence integration.
- WS-C and WS-D can proceed in parallel after the model contract is stable.
- WS-E consumes the model and catalog contracts; UI work must not invent a separate source of truth.
- WS-G runs continuously and blocks promotion when tests, schema checks, license review or evidence are missing.

## Current implementation evidence
- Python model core and deterministic validation are present.
- SQLite local persistence uses transactions and optional optimistic revision checks.
- Typed form validation supports required, type, range, enum, pattern and unknown-field checks.
- Catalog contains 14 card types, 12 board types, 10 card views and 5 starter Decks.
- Browser prototype supports Board, searchable Gallery, Deck Library, Inspector editing, local demo persistence and JSON export.
- EKTA taxonomy crosswalk is checked against current YAML registries by automated tests.
- CI includes repository tests, VES tests, schema JSON parsing, browser JavaScript syntax checks, documentation validation and graph export.

## Required engineering loop
Test → Evaluate → Identify Deviation → Correct → Retest → Re-evaluate. Each behavior change adds or updates a focused test before implementation. A test pass is tied to an exact commit SHA and workflow run.

## Current branch and CI snapshot
- PR #20 is open as draft and mergeable; it must not be merged without owner review.
- Branch is 13 commits ahead of main and 0 commits behind at this snapshot.
- CI on crosswalk implementation head fa6fd937083209da1070eaaa7394db4b6ef133d7 passed (runs 45304206018 and 45304213142).
- CI on the latest schema head 807848d3c85efe6f8f26c56ec197fbb9e13dd6dc is running (runs 45304629419 and 45304636491). Do not report latest-head PASS until both finish successfully.

## Next execution queue
1. Confirm latest-head CI, inspect logs and correct any failing step.
2. Add full JSON Schema runtime validation to import/export boundaries.
3. Add explicit project file import with preview, validation and no-overwrite conflict policy.
4. Add Deck and Board persistence to the canonical model, not just catalog templates.
5. Add form builder UI and connect field definitions to the typed form validator.
6. Add board type switcher, multiple boards per project and typed relationship editing.
7. Add asset provenance, checksum and license capture.
8. Evaluate production React/TypeScript client only after the interaction contract is stable.
9. Add Android/Windows packaging and device QA after offline persistence is hardened.

## Promotion gates
- G1: schema and model contract reviewed.
- G2: focused tests and full CI green on exact head.
- G3: import/export round-trip and no-data-loss report.
- G4: license/security review for selected dependencies.
- G5: browser, Windows and Android claims backed by target-platform tests.
- G6: owner review and explicit PR merge approval.

## Explicit non-claims
The current browser application is a prototype, not a production-ready editor. Full SysML/UML/BPMN/EDA/CAD conformance, simulation, collaboration, plugin sandboxing, mobile/desktop packaging and release signing remain unimplemented or NOT RUN.
