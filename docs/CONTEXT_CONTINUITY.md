# EKTA Context Continuity Protocol

## Canonical resumption order
1. README.md
2. docs/USER_DOCUMENTATION_INDEX.md for end users; docs/PROJECT_CHARTER.md and docs/GOVERNANCE.md for project scope
3. docs/PROJECT_OVERVIEW.md and docs/KNOWLEDGE_ARCHITECTURE.md
4. docs/KNOWLEDGE_OPERATING_WORKFLOW.md and docs/AGENT_ONBOARDING.md
5. docs/IMPLEMENTATION_PLAN.md and docs/ROADMAP.md
6. docs/RUNTIME_ARCHITECTURE.md and CHANGELOG.md
7. latest relevant ADR/RFC
8. relevant taxonomy, schemas, records, runtime services, tests, and current GitHub Actions

## Non-negotiable rules
- Git repository is canonical project memory; chat memory is supplemental.
- An idea discussed in chat is not approved or committed by default.
- Record decisions in ADRs; unresolved proposals in RFCs.
- Separate intended design from implementation state.
- Preserve rejected alternatives and rationale when useful.
- Do not merge unrelated projects without explicit authorization.
- Do not silently change scope, IDs, schemas, or license.
- Inspect branch and repository state before editing.
- Report exact paths, commit/PR references, validation performed, and anything NOT_RUN.
- User documentation must describe the released code, not planned features.
- Update installation/manual/input documentation when runtime behavior changes.

## Current repository handoff — 2026-11-23

- Canonical repository: https://github.com/metsam-mastem/EKTA
- Default branch: main
- Documentation branch: docs/user-independence-v0.3
- Documentation PR: #4, merged
- Documentation merge commit: 82c2e8a58f7c8449a440822183d30a8fdf81a73f
- Baseline before documentation work: d66d8b13b8d24200af91f07c51b2df01ec131bcd
- Current repository handoff must be refreshed from the live main HEAD before any new implementation.
- Scope: Persian-first user documentation, setup, installation, manual, input/ingestion boundaries, recovery, troubleshooting, and AI/developer onboarding.
- Product baseline: Search/Explore Runtime 0.2 plus Operational Workspace 0.4; canonical knowledge remains Git-native and read-only from the UI.
- Runtime facts: Python 3.11+, FastAPI/Uvicorn, PyYAML, JSON Schema; local default 127.0.0.1:8000; selected Markdown/YAML/JSON indexing; deterministic lexical search.
- Known limitations: import is text-only staging (not canonical ingestion); editor creates local drafts only; restore only stages validated ZIPs; no semantic/AI search, auth/multi-user, public deployment hardening, Android package, or full Decision/Execution Labs.
- License remains undecided.
- Graph coverage remains incomplete; never present graph export as a complete ontology.
- PR #3 (integration/upds-documentation-architecture) is CLOSED, NOT MERGED, and superseded by clean-mainline PR #23 (integration/upds-independent-continuity). UPDS integration remains PROPOSED pending owner review of EKTA-ADR-0003.
- Validation passed on documentation PR head d1463eefe9e7ceb17c8fdf39b862a2a10c04e12c: docs validation, 29 tests, frontend structural/JavaScript validation, and graph export. Post-merge CI on main is tracked separately.
- For a chat-independent continuation, this file plus README, Project Overview, Implementation Plan, Roadmap, Changelog, and current GitHub PR/Actions state are sufficient starting points.

## Operational Workspace v0.4 — PR #5

- Branch: `workbench/operational-suite-v0.4`
- PR: https://github.com/metsam-mastem/EKTA/pull/5
- Scope: onboarding wizard, first-run self-test, import staging, draft editor, backup/restore preview, documentation center.
- New runtime module: `runtime/ekta_runtime/workspace.py`; new UI: `runtime/web/workspace.html`; API routes under `/api/v1/workspace/`.
- Local staging root: `.ekta/workspace/`; `.ekta/` is gitignored.
- Import formats: Markdown/YAML/JSON text, max 1 MiB. Drafts remain outside `encyclopedia/concepts/`.
- Backup uses an explicit project path allowlist and excludes `.git`, environments, caches and secret files. Restore only validates and stores the ZIP; it never extracts or overwrites project files.
- Canonical Git knowledge remains protected; no automated promotion, Git commit/push, authentication, or public deployment hardening.
- Added `tests/test_workspace.py`; GitHub Actions run #146 on PR #5 head `37d8e892aa9cf9210c43231f5ffcf9464f67bcb7` completed SUCCESS (docs validation, unit/runtime tests, frontend validation, graph export).
- Detailed user and security docs: `docs/WORKSPACE_GUIDE.md`, `docs/SECURITY_AND_STAGING_MODEL.md`.
- PR #6 (`workbench/verification-hardening-v0.4`) merged as `883451d022eee25b5d59c21cf5f4aaa391a7a396`; CI run #176 on head `99c5870d14f3659d3a71147f9a97b49d1bf7064c` completed SUCCESS. It adds strict concept ID validation, duplicate-ID protection, bounded draft metadata, malformed YAML and restore traversal tests, and workspace frontend syntax/structure checks.
- Post-merge documentation line-break cleanup, explorer navigation/API table refinements, setup/installation updates, and UI hardening were committed directly to main; the latest main HEAD must be read before the next code change.

## Session handoff template
### Objective
### Confirmed decisions
### Repository revision
### Artifacts changed
### Evidence collected
### Tests/validation
### Open questions
### Risks/blockers
### Next smallest actionable step

## Missing context
Mark missing facts UNKNOWN. Do not guess. Conflicts between sources and decisions must be preserved and escalated for review.

## Memory hierarchy
Approved repository artifacts > accepted ADRs > verified sources and test evidence > issues/PRs > conversation summaries > unverified suggestions.


## Parallel orchestration snapshot — 2026-11-24

- Registry: `orchestration/WORKSTREAMS.yml`.
- Execution plan: `docs/ORCHESTRATION/ACTIVE_WORKSTREAMS.md`.
- Integration matrix: `docs/ORCHESTRATION/INTEGRATION_MATRIX.md`.
- Validation: `tools/validate_orchestration.py`; tests: `tests/test_orchestration.py`; schema: `schemas/workstream-registry.schema.json`.
- Ten active product workstreams are tracked in the YAML registry; PR #21 is the orchestration PR. No subsystem PR was merged by the orchestration setup.
- Main revision observed during comparison: `7ea271e00ef2cb010c17bdaa553e1f27645f12ca`.
- PR #3 is closed/unmerged and superseded by clean-mainline UPDS PR #23; its branch was 57 ahead / 35 behind. PR #23 is 75 ahead / 0 behind and latest exact-head CI run #408 passed.
- Several subsystem PR branches remain one commit behind main; their exact-head CI passes do not remove the branch-freshness gate.
- No unattended background process is active. GitHub registry, PRs, and Actions are durable continuation state.


## GTC integration and archive identity conflict — 2026-11-24

- EKTA main commit `7ea271e00ef2cb010c17bdaa553e1f27645f12ca` pins GTC at `integrations/gtc`, upstream commit `2f0229bd622de4e9ce22196e57fb986659dc7934`.
- Integration audit: `docs/integrations/GTC_INTEGRATION.md`; canonical Hardware Knowledge Atlas record: `encyclopedia/concepts/EKTA-CON-000008-hardware-knowledge-atlas.md`.
- PR #7 stages Operating System under the same ID `EKTA-CON-000008`. This is a confirmed collision; archive intake is BLOCKED pending owner-approved immutable ID correction. Do not promote the staged record or transfer the remaining 14 records until manifest and hash/provenance mapping are reconciled.
- Machine-readable orchestration tracks the GTC pin and archive block in `orchestration/WORKSTREAMS.yml`.\n- Orchestration PR #21 latest exact head `ddca9dbe92edd5170d3e30bcd0b26773a067647a` passed Actions run #438; documentation, registry validation, unit/runtime tests, frontend checks, and graph export all passed.\n- PR #22 Engineering Organization Crosswalk exact head `bf759902809282713d2c2a9354070132d702a150` passed run #289; the 14-area map remains non-canonical.\n- PR #23 UPDS exact head `8453a2d179490969a5b2262c8d8e34ba957d3d5c` passed run #408; clean-clone recovery is still NOT RUN.
