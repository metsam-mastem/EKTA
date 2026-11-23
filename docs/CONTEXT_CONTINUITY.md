# EKTA Context Continuity Protocol

## Canonical resumption order
1. README.md
2. docs/PROJECT_CHARTER.md and docs/GOVERNANCE.md
3. docs/KNOWLEDGE_ARCHITECTURE.md and docs/KNOWLEDGE_OPERATING_WORKFLOW.md
4. docs/IMPLEMENTATION_PLAN.md and docs/CONTEXT_CONTINUITY.md
5. CHANGELOG.md
6. latest relevant ADR/RFC
7. relevant taxonomy, schemas, records, and runtime services
8. open issues, pull requests, GitHub Actions, and current branch state

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

## Current runtime handoff — 2026-11-23

- Mainline baseline before v0.2 work: `0d53a9131dad1aeca4c909493871b2ad7b41a225`.
- Active development branch: `workbench/v0.2-explorer`.
- Scope in progress: deterministic unified search; hashtag/fielded query parsing; 26 territory and 25 operational domain taxonomy; Persian RTL explorer; scoped concept/document identity cards; coherent knowledge intake and PR gates.
- Expected validation: schema/taxonomy validator, complete unittest suite, graph export. No browser-based manual QA or hosted deployment should be claimed unless separately performed.
- Current constraints: canonical Git Markdown/YAML remains authoritative; runtime search is lexical (not semantic); runtime remains read-only; license is undecided.

## Session handoff
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


## UPDS integration resumption

For work on the UPDS integration, read in this order:
1. `docs/INTEGRATION/UPDS_INTEGRATION_INDEX.md`
2. `docs/INTEGRATION/UPDS_EKTA_INTEGRATION_DECISION.md` (PROPOSED until owner approval)
3. `docs/INTEGRATION/UPDS_EKTA_SYSTEM_ARCHITECTURE.md`
4. `docs/INTEGRATION/UPDS_DOCUMENT_UNIVERSE.md`
5. `docs/INTEGRATION/UPDS_EKTA_CROSSWALK.md`
6. `docs/INTEGRATION/UPDS_PROJECT_MEMORY_AND_CHAT_INDEPENDENCE.md`
7. `docs/PROJECT_STATE.md`, `docs/ACTIVE_WORK.md`, `docs/OPEN_ISSUES.md`, `docs/EVIDENCE_INDEX.md`, `docs/SESSION_HANDOFF.md`

The integration branch is `integration/upds-documentation-architecture`. Its current work is documentation-only. Do not claim runtime integration or passing tests until the branch CI evidence exists.
