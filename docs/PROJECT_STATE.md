# EKTA Project State
**Snapshot date:** 2026-11-24  
**Canonical repository:** https://github.com/metsam-mastem/EKTA  
**Default branch:** main  
**Working branch:** integration/upds-independent-continuity  
**Replacement PR:** https://github.com/metsam-mastem/EKTA/pull/23  
**Branch origin:** main at 7ea271e00ef2cb010c17bdaa553e1f27645f12ca

## Product identity and baseline
EKTA is an independent, evidence-backed engineering knowledge environment with DISCOVERY, ENCYCLOPEDIA, DECISION LAB and EXECUTION LAB. Git, approved decisions and test evidence are canonical; chat/model memory is supplemental.

Current documented baseline: Runtime 0.2 + Operational Workspace 0.4. Workspace supports bounded Markdown/YAML/JSON staging, local drafts, self-test, documentation center, ZIP backup and safe restore preview. It does not automatically write canonical records. Search is lexical, not semantic. Direct PDF/Office/image/audio/video/CAD ingestion, Android APK, auth/multi-user cloud and public production hardening are not claimed. License remains undecided.

## UPDS integration
UPDS is proposed as a bounded, cross-cutting, separable subsystem for project-scoped documents, requirements, decisions, architecture records, risks/changes, evidence, configuration, traceability and durable project memory.
- Architecture/catalog/crosswalk/roadmap/input model/runtime blueprint: DOCUMENTED.
- Base JSON Schema, sample record, validator and tests: VERIFIED.
- Read-only repository Document Registry (list/get) and GET API endpoints: VERIFIED.
- Chat-independent continuity manifest validator and tests: VERIFIED.
- Registry write/update lifecycle, audit history, full graph traceability, dashboard and project starter: NOT IMPLEMENTED.
- Clean-clone human recovery and independent backup restore: NOT RUN.
- Integration ADR: PROPOSED; owner review required.

## Branch and PR status
- Old branch integration/upds-documentation-architecture: diverged 57 ahead / 35 behind main at comparison; do not merge.
- Old PR #3: CLOSED, NOT MERGED; superseded by PR #23. Old branch/history preserved.
- New branch integration/upds-independent-continuity: created from main and remained based on main in the latest comparison.
- PR #23: OPEN, DRAFT, not merged.
- PR #4 user docs: CLOSED; Persian-first docs are present in main and linked from this branch.
- Other EKTA proposal streams remain separate; inspect their live status before action.

## Verification evidence
GitHub Actions run 45305319405 completed SUCCESS on exact commit 8453a2d179490969a5b2262c8d8e34ba957d3d5c. Passed: dependency installation, documentation/link validation, UPDS record validation, chat-independent continuity manifest validation, full unittest discovery (including registry and continuity tests), frontend validation and typed graph export.
Run 45304968576 also passed on exact commit 1c06074a8d31b87602b4426cb70640a8b26571aa, verifying the registry slice before the continuity validator was added.
Run 45305226654 failed because the continuity manifest contained literal escaped newlines; this was diagnosed from logs, corrected, and superseded by the successful run above.

## Constraints
Do not merge PR #23 or promote ADR-0003 without explicit owner approval. Do not alter license/taxonomy silently, add hosted dependencies without ADR, merge unrelated projects, delete canonical content or claim unverified behavior. Use TDD for code changes.

## Next actions
1. Review proposed EKTA-ADR-0003.
2. Run clean-clone human recovery without chat.
3. Create a portable backup, checksum it, restore to a new directory and rerun validation.
4. Design controlled draft/write/revision lifecycle with TDD.
5. Implement typed traceability vertical slice.
6. Build dashboard and project starter after contract stabilization.
