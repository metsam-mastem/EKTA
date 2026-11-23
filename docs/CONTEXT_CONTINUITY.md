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
- Default branch before this documentation change: main
- Baseline main commit: d66d8b13b8d24200af91f07c51b2df01ec131bcd
- Documentation work branch: docs/user-independence-v0.3
- Scope: Persian-first user documentation, setup, installation, manual, input/ingestion boundaries, recovery, troubleshooting, and AI/developer onboarding.
- Product baseline: Runtime 0.2; read-only local web application.
- Runtime facts: Python 3.11+, FastAPI/Uvicorn, PyYAML, JSON Schema; local default 127.0.0.1:8000; selected Markdown/YAML/JSON indexing; deterministic lexical search.
- Known limitations: no UI upload/edit, semantic/AI search, auth/multi-user, public deployment hardening, Android package, or full Decision/Execution Labs.
- License remains undecided.
- Graph coverage remains incomplete; never present graph export as a complete ontology.
- Validation must be run on the final documentation branch and after merge on main.

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
