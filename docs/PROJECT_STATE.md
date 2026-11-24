# EKTA Project State
**Snapshot date:** 2026-11-24  
**Canonical repository:** https://github.com/metsam-mastem/EKTA  
**Default branch:** main  
**Clean UPDS continuation branch:** integration/upds-independent-continuity  
**Branch origin:** main at 7ea271e00ef2cb010c17bdaa553e1f27645f12ca  
**Replacement PR:** https://github.com/metsam-mastem/EKTA/pull/23

## Product identity and current baseline
EKTA (Engineering Knowledge & Techniques Atlas) is an independent, evidence-backed engineering knowledge environment with four workspaces: DISCOVERY, ENCYCLOPEDIA, DECISION LAB and EXECUTION LAB. The Git repository, approved decisions and test evidence are canonical; chat/model memory is supplemental.

Current documented product baseline: Runtime 0.2 + Operational Workspace 0.4. Workspace supports bounded Markdown/YAML/JSON staging, local drafts, self-test, documentation center, ZIP backup and safe restore preview. It does not automatically write canonical records. Search is lexical, not semantic. Direct PDF/Office/image/audio/video/CAD ingestion, Android APK, auth/multi-user cloud and public production hardening are not claimed. License remains undecided.

## UPDS integration
UPDS is proposed as a bounded, cross-cutting, separable subsystem for project-scoped documents, requirements, decisions, architecture records, risks/changes, evidence, configuration, traceability and durable project memory.
- Architecture/catalog/crosswalk/roadmap/input model/runtime blueprint: DOCUMENTED.
- Base JSON Schema, sample record, validator and tests: IMPLEMENTED on branch.
- UPDS validator CI step: IMPLEMENTED on branch.
- Runtime registry/API, complete graph traceability, dashboard and project starter: NOT IMPLEMENTED.
- Clean-clone recovery and independent backup restore: NOT RUN.
- Integration ADR: PROPOSED; owner review required.

## Branch and PR status
- Old branch `integration/upds-documentation-architecture`: diverged 57 ahead / 35 behind main at comparison; do not merge as-is.
- Old PR #3: CLOSED, NOT MERGED, explicitly superseded by PR #23. Original branch/history preserved.
- New branch `integration/upds-independent-continuity`: created from main; compare result 48 commits ahead, 0 behind at last check.
- Replacement PR #23: OPEN, DRAFT, not merged; branch is based on current main.
- PR #4 user documentation: CLOSED; canonical Persian-first user docs are present in main and linked from this branch.
- Other EKTA proposal streams remain independent; inspect their live status before action.

## Verification evidence
GitHub Actions run 45304523297 completed SUCCESS on commit 11ac9b7689b366299e7856a814cae289c63b4e24. Steps passed: dependency install, documentation/link validation, UPDS record validation, full unittest discovery, frontend HTML/JavaScript validation and typed graph export. This pass applies only to that exact commit. Subsequent documentation/orchestration commits are not covered by that run; latest-head CI must be checked separately.

## Constraints
Do not merge PR #23 or promote ADR-0003 without explicit owner approval. Do not alter license/taxonomy silently, add hosted database/cloud dependencies without ADR, merge unrelated projects, delete canonical content or claim unverified behavior. Use TDD for code changes.

## Next actions
1. Check CI on the latest PR #23 head; repair any failures.
2. Review proposed EKTA-ADR-0003 and decide approve/revise/reject.
3. Run clean-clone recovery without chat.
4. Create a portable backup, checksum it, restore into a new directory and rerun validation.
5. Implement repository-backed registry/API with TDD.
6. Implement typed traceability vertical slice.
7. Build dashboard and project starter after contract stabilization.
