# EKTA Project State
**Snapshot date:** 2026-11-24  
**Canonical repository:** https://github.com/metsam-mastem/EKTA  
**Default branch:** main  
**Clean UPDS continuation branch:** integration/upds-independent-continuity  
**Baseline used to create continuation branch:** 7ea271e00ef2cb010c17bdaa553e1f27645f12ca

## Product identity
EKTA (Engineering Knowledge & Techniques Atlas) is an independent, evidence-backed engineering knowledge environment. Its canonical product workspaces are DISCOVERY, ENCYCLOPEDIA, DECISION LAB and EXECUTION LAB. The repository is the durable source of truth; conversation history is non-canonical.

## Current product baseline
- Runtime: 0.2 Search & Explore Workbench.
- Operational Workspace: 0.4, including onboarding/self-test, bounded Markdown/YAML/JSON staging, local drafts, documentation center, ZIP backup and safe restore preview.
- Current documented limits: no semantic/AI search, no direct PDF/Office/image/audio/video ingestion, no authentication or multi-user cloud, no Android APK, and no automatic canonical promotion/restore.
- License remains undecided.

## UPDS integration status
UPDS (Universal Project Documentation System) is proposed as a cross-cutting, separable subsystem for project-scoped documentation, requirements, architecture records, decisions, risks/changes, evidence, configuration, traceability and project memory.
- Architecture/catalog/crosswalk/roadmap and input/runtime contracts: DOCUMENTED.
- Base schema, sample record, validator and tests: IMPLEMENTED on integration branch.
- CI step for UPDS validator: added to this branch; latest branch CI result pending.
- Runtime registry/API, full graph traceability, dashboard and project starter: NOT IMPLEMENTED.
- Clean-clone recovery and independent backup restore: NOT RUN.
- Integration ADR: PROPOSED; owner review required.

## Branch and PR status at snapshot
- Old branch `integration/upds-documentation-architecture` is DIVERGED from current main (57 commits ahead, 35 behind at comparison). Do not merge it as-is.
- Old PR #3 remains open and should be superseded only after the clean replacement PR is available.
- New branch `integration/upds-independent-continuity` was created from main at the baseline SHA above and receives a selective additive port of UPDS content plus this session's archive.
- PR #4 user documentation change is closed; its Persian-first documentation index is present on main.
- Other proposal streams (#7, #8, #9, #10, #11, #12, #13, #19, #20) remain separate scopes; inspect live status before action.

## Non-negotiable constraints
Do not merge without owner approval; do not alter license or taxonomy silently; do not add hosted database/cloud dependencies without an ADR; do not merge unrelated projects; preserve stable IDs and history; use TDD for behavior changes; record exact evidence.

## Next actions
1. Complete and verify the clean port and conversation archive on this branch.
2. Confirm documentation links, schema validity and UPDS tests via CI on exact branch head.
3. Open replacement PR and link stale PR #3 as superseded; preserve its branch/history.
4. Review and approve/revise EKTA-ADR-0003.
5. Run clean-clone recovery and independent backup restore.
6. Implement registry/API, typed traceability, dashboard and project starter in separate tested slices.
