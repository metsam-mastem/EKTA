# VES Development Orchestration

**Baseline:** 0.1.0 · **Repository:** metsam-mastem/EKTA  
**Branch:** project/ves-foundation-v0.1 · **Review:** PR #20 (draft; unmerged)

## Operating rule
One VES project namespace, one integration branch and one review path. Workstreams may be developed independently, but artifacts converge on one versioned model and acceptance criteria. No direct writes to EKTA main and no merging unrelated project streams.

## Workstreams
| ID | Workstream | Scope | Dependency | Exit evidence |
|---|---|---|---|---|
| WS-A | Product and architecture | product brief, system boundaries, ADRs, layer model | none | reviewed spec and ADR |
| WS-B | Canonical model and schemas | Entity, Relationship, Board, Placement, Project, JSON contracts | WS-A | schema and round-trip tests |
| WS-C | Persistence and interchange | SQLite store, revisions, import/export and migration | WS-B | persistence and conflict tests |
| WS-D | Card, Deck and Form systems | type catalog, views, Decks, typed field validation | WS-B | catalog/form tests |
| WS-E | Visual workspace | Board, Inspector, Gallery, Deck views and touch behavior | WS-B, WS-D | browser interaction and responsive QA |
| WS-F | EKTA knowledge integration | taxonomy crosswalk, provenance and project registration | EKTA registries | crosswalk test and review |
| WS-G | Quality, security and release | CI, schema validation, license review, test evidence and packaging | all workstreams | green CI and release checklist |

## Parallelization
- WS-A and WS-F can progress independently.
- WS-B is the shared contract and must stabilize before deep UI or persistence integration.
- WS-C and WS-D can proceed in parallel after the model contract is stable.
- WS-E consumes model and catalog contracts; UI must not invent a second source of truth.
- WS-G runs continuously and blocks promotion when tests, schema checks, license review or evidence are missing.

## Current implementation evidence
- Python model core and deterministic validation.
- SQLite local persistence with transactional writes and optional optimistic revision checks.
- Typed form validation for required, type, range, enum, pattern and unknown-field checks.
- Catalog with 14 card types, 12 board types, 10 card views and 5 starter Decks.
- Browser prototype with Board, searchable Gallery, Deck Library, Inspector editing, local demo persistence and JSON export.
- EKTA taxonomy crosswalk checked against current YAML registries by automated tests.
- Research brief compares notation standards and candidate OSS integration boundaries.

## Required engineering loop
Test → Evaluate → Identify Deviation → Correct → Retest → Re-evaluate. Every behavior change adds or updates a focused test before implementation. A test pass is tied to an exact commit SHA and workflow run.

## Verified CI snapshot
- Verified head: 46ea893f393bf5a0ea45e68358611b044b61a3b7.
- GitHub Actions run 45304786770 completed SUCCESS.
- EKTA repository suite: 39 tests passed.
- VES suite: 19 tests passed.
- Documentation validation, schema checks, browser JavaScript syntax, frontend validation and knowledge-graph export passed.
- This research-documentation commit creates a new head and must receive its own CI run before status is marked PASS.

## Next execution queue
1. Verify CI on the research-documentation head.
2. Add full JSON Schema runtime validation to import/export boundaries.
3. Add explicit project file import with preview, validation and no-overwrite conflict policy.
4. Add Deck and Board persistence to the canonical model, not just catalog templates.
5. Add Form Builder UI and connect field definitions to typed validation.
6. Add board type switcher, multiple boards per project and typed relationship editing.
7. Add asset provenance, checksum and license capture.
8. Evaluate production React/TypeScript client only after the interaction contract is stable.
9. Add Android/Windows packaging and device QA after offline persistence is hardened.

## Promotion gates
G1 model/schema review; G2 exact-head CI green; G3 import/export round-trip and no-data-loss report; G4 license/security review; G5 platform claims backed by target tests; G6 owner review and explicit PR merge approval.

## Explicit non-claims
The browser application is a prototype, not production-ready. Full SysML/UML/BPMN/EDA/CAD conformance, simulation, collaboration, plugin sandboxing, mobile/desktop packaging and release signing remain unimplemented or NOT RUN.
