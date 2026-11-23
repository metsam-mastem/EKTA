# EKTA Project Administration Guide
**Document ID:** EKTA-USER-ADMIN-0001 | **Status:** DOCUMENTATION BASELINE

## Authority
Git history and canonical repository files are authoritative. Chat, issue comments and personal notes may provide context but cannot override approved decisions. The owner approves scope, architecture, licensing, destructive changes, releases and external integrations.

## Core registers
Maintain PROJECT_STATE (state/branch/commit), DECISION_REGISTER (rationale/alternatives/approval), ACTIVE_WORK (packages/status/next actions), OPEN_ISSUES (blockers), CONSTRAINTS_AND_ASSUMPTIONS, EVIDENCE_INDEX and SESSION_HANDOFF. UPDS architecture and catalog live under docs/INTEGRATION. Update relevant registers with each meaningful implementation change.

## Decision lifecycle
PROPOSED → REVIEWED → APPROVED or REJECTED → IMPLEMENTED → VERIFIED/VALIDATED where applicable. Approval is not implementation; implementation is not validation. Record approver and date.

## Change control
Identify affected records, schemas, APIs, taxonomy, graph relations, users and migration risks. Add tests for behavior changes. Prefer additive migrations. Preserve IDs and history. Risky changes require rollback/recovery notes. Never delete or rename canonical records without migration mapping and explicit approval.

## Release management
A release needs version, scope, changelog, reproducible build, platform matrix, dependency inventory, license/security review, tests, known limitations and rollback instructions. A green unit test alone is not release readiness.

## Backup and access
Keep remote Git plus an independent mirror or periodic Git bundle. Test restoration. Use least privilege, separate read/write access and credential managers. Never commit secrets. Revoke compromised credentials.

## Operational review
At milestones, review project state, open issues, CI, dependency/security alerts, stale decisions, broken links, evidence coverage and recovery readiness. No scheduled automation is implied.
