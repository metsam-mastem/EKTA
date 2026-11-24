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
- PR #3 (integration/upds-documentation-architecture) is a separate open proposal. Its integration decision is PROPOSED pending explicit owner review; do not treat UPDS integration as approved or merged based only on the branch.
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


## UPDS and chat-independent continuity snapshot — 2026-11-24

The current clean continuation work is on `integration/upds-independent-continuity`, created from main at `7ea271e00ef2cb010c17bdaa553e1f27645f12ca`. The earlier `integration/upds-documentation-architecture` branch diverged from current main (57 ahead / 35 behind at the 2026-11-24 comparison) and must not be merged as-is. PR #3 remains open pending supersession by a clean replacement PR.

Read [UPDS Integration Index](INTEGRATION/UPDS_INTEGRATION_INDEX.md), [Project State](PROJECT_STATE.md), [Conversation Context Archive](PROJECT_CONTINUITY/CHAT_SESSION_ARCHIVE_2026-11-24.md), [Agent Onboarding](PROJECT_CONTINUITY/AGENT_ONBOARDING.md), and [Recovery Runbook](PROJECT_CONTINUITY/RECOVERY_RUNBOOK.md).

The canonical Persian-first user documentation remains [USER_DOCUMENTATION_INDEX.md](USER_DOCUMENTATION_INDEX.md). Do not create parallel manuals.

UPDS architecture is PROPOSED; the base schema, validator and test source are implemented on the continuation branch, but latest-head CI is pending. Registry/API, complete typed traceability, dashboard and project starter are NOT IMPLEMENTED. Clean-clone recovery and independent backup restore are NOT RUN. Historical CI evidence is commit-specific and must not be reused for this branch.

The archive is a structured summary, not a verbatim ChatGPT transcript. Repository state supersedes conversation summaries.
