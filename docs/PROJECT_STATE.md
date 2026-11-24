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
- Base JSON Schema, sample record, validator and tests: IMPLEMENTED on branch.
- Read-only repository Document Registry (list/get) and GET API endpoints: IMPLEMENTED on branch; latest test run pending.
- Registry write/update lifecycle, audit history, full graph traceability, dashboard and project starter: NOT IMPLEMENTED.
- Clean-clone recovery and independent backup restore: NOT RUN.
- Integration ADR: PROPOSED; owner review required.

## Branch and PR status
- Old branch integration/upds-documentation-architecture: diverged 57 ahead / 35 behind main at comparison; do not merge.
- Old PR #3: CLOSED, NOT MERGED; superseded by PR #23. Old branch/history preserved.
- New branch integration/upds-independent-continuity: based on main; latest comparison 58 commits ahead, 0 behind.
- PR #23: OPEN, DRAFT, not merged.
- PR #4 user docs: CLOSED; Persian-first docs are present on main and linked from this branch.
- Other EKTA proposal streams remain separate; inspect live status before action.

## Verification evidence
Run 45304714331 completed SUCCESS on commit fdd995f173c7d51a777f9e841172c648b4af3cad. It passed dependency installation, documentation/link validation, UPDS record validation, full unittest discovery, frontend validation and typed graph export. This verifies docs/schema/validator/tests as of that SHA, before the read-only registry implementation.
Run 45304839153 was queued for the registry implementation commit; the current registry tests and API updates are newer than that commit and latest-head CI must be checked.
Historical run 45304523297 also passed at 11ac9b7689b366299e7856a814cae289c63b4e24 only.

## Constraints
Do not merge PR #23 or promote ADR-0003 without explicit owner approval. Do not alter license/taxonomy silently, add hosted dependencies without ADR, merge unrelated projects, delete canonical content or claim unverified behavior. Use TDD for code changes.

## Next actions
1. Check CI on latest PR #23 head and fix any failing registry tests.
2. Review proposed EKTA-ADR-0003.
3. Run clean-clone recovery without chat.
4. Create a portable backup, checksum it, restore to a new directory and rerun validation.
5. Extend registry to controlled draft/write/revision lifecycle with TDD.
6. Implement typed traceability vertical slice.
7. Build dashboard and project starter after contract stabilization.
