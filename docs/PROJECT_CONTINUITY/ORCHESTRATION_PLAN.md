# UPDS Delivery Orchestration Plan
**Document ID:** EKTA-ORCH-UPDS-0001  
**Snapshot:** 2026-11-24  
**Execution mode:** dependency-aware parallel work packages with serialized integration

## 1. Objective
Deliver UPDS as a reliable, separable project-documentation subsystem while preserving EKTA's current product, taxonomy, history and independent project boundaries. Make project continuation possible without ChatGPT history.

## 2. Orchestration rules
- Parallelize research, independent specifications and isolated tests where file ownership does not overlap.
- Serialize edits to shared files: README, CI workflow, project state, shared schemas and canonical taxonomy.
- Each work package has a defined owner, input contract, output artifacts, acceptance criteria and evidence.
- Use TDD for all behavior changes: RED test → GREEN implementation → REFACTOR → full regression.
- Integration is gated by contracts and CI; no speculative API/UI before data model review.
- A workstream is not complete because its document exists.
- Do not merge without explicit owner approval.
- This plan does not create persistent background execution. Work proceeds only during an active authorized session or configured automation.

## 3. Work packages

| WP | Stream | Scope | Can run in parallel with | Gate / dependency |
|---|---|---|---|---|
| ORCH-00 | Continuity & governance | archive, handoff, manifest, recovery, decision control | ORCH-01, ORCH-05 | Clean-clone and restore drills |
| ORCH-01 | Data contracts | artifact schema, status dimensions, IDs, typed relations | ORCH-00, ORCH-05 | Owner review and schema tests |
| ORCH-02 | Registry core | repository-backed CRUD/read service, revisions, validation, audit | ORCH-05 | ORCH-01 contract frozen |
| ORCH-03 | Traceability graph | requirement/decision/component/test/run/evidence/release edges and gap reports | ORCH-02 design can proceed; implementation after ORCH-02 | Registered relation vocabulary |
| ORCH-04 | User experience | registry explorer, completeness dashboard, project starter | ORCH-02 and ORCH-03 design | Stable API and user-flow acceptance |
| ORCH-05 | QA, security and evidence | unit/integration tests, schema/link validation, path/size/secret controls, CI | all streams | Exact SHA test evidence |
| ORCH-06 | Standards and OSS research | compare document/requirements/configuration standards and OSS patterns | all streams | Source register; no dependency adoption without review |

## 4. Delivery phases and exit criteria

### Phase A — Baseline and continuity (active)
- Clean branch based on current main.
- Conversation context archive and canonical navigation.
- Project state and evidence registers.
- UPDS schema/validator/CI gate.
- Exit: CI passes on exact branch head; clean-clone recovery and backup restore are demonstrated.

### Phase B — Contract stabilization
- Review artifact identity, status dimensions, relation vocabulary and project boundaries.
- Define compatibility/versioning and migration rules.
- Exit: accepted ADR and schema contract with examples and negative tests.

### Phase C — Registry vertical slice
- Add project and document records with deterministic ID rules, schema validation, revision history and repository-backed persistence.
- Start with local/Git-native storage; no hosted database.
- Exit: create/list/get/update with optimistic concurrency or explicit immutable revision semantics, audit trail and integration tests.

### Phase D — Traceability vertical slice
- Link one objective/source to a requirement, decision, component, test case, test run, evidence and release.
- Report unresolved edges and gaps explicitly.
- Exit: queryable end-to-end traceability with tests; no inferred satisfaction.

### Phase E — Workbench and generator
- Build read-only registry explorer first, then controlled local write flows.
- Generate tailored project skeletons from project type/risk profile.
- Exit: user tests, completeness checks, export/clone and recovery.

### Phase F — Extraction readiness
- Verify UPDS can be used by a second sample project without EKTA runtime coupling.
- Document package boundary, schema compatibility and migration path.
- Exit: independent reuse test and owner decision on standalone package/repository.

## 5. Critical path
`ADR review → schema/status/relation contract → registry core → traceability → dashboard/project starter → extraction test`.

Continuity, QA and OSS research can run alongside the critical path. Runtime implementation must not bypass contract gates.

## 6. Definition of done
For every work package:
- deliverables and changed paths are linked;
- acceptance criteria are measurable;
- tests are run and results attached to exact commit;
- security and license boundaries are reviewed;
- state/decision/evidence/handoff registers are updated;
- next dependency and owner action are explicit.

## 7. Current state
- ORCH-00: documentation foundation IMPLEMENTED; clean-clone and backup drills NOT RUN.
- ORCH-01: initial schema IMPLEMENTED; status/relation contract review BLOCKED pending owner.
- ORCH-02: read-only registry list/get service and API VERIFIED by CI run 45304968576 on commit 1c06074a8d31b87602b4426cb70640a8b26571aa. Write/update/revision lifecycle remains NOT IMPLEMENTED.
- ORCH-03: NOT IMPLEMENTED.
- ORCH-04: NOT IMPLEMENTED.
- ORCH-05: UPDS validator added to CI; current workflow must finish on exact PR head.
- ORCH-06: candidate research scope identified; no new dependencies selected.
