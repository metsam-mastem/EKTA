# Active Work Register
**Baseline:** integration/upds-independent-continuity  
**Snapshot:** 2026-11-24

| ID | Work package | Status | Next action |
|---|---|---|---|
| UPDS-WP-001 | Port UPDS architecture/catalog to current main | IMPLEMENTED | review PR #23 |
| UPDS-WP-002 | Integration ADR owner decision | BLOCKED | approve/revise EKTA-ADR-0003 |
| UPDS-WP-003 | Base schema, fixture and validator | VERIFIED at 1c06074 | retain exact CI evidence |
| UPDS-WP-004 | CI gate and unit tests | VERIFIED at 1c06074 | maintain as merge gate |
| UPDS-WP-005 | Canonical user docs and navigation | IMPLEMENTED | maintain one Persian-first manual |
| UPDS-WP-006 | Chat archive, manifest and agent onboarding | IMPLEMENTED as structured docs | raw transcript export unavailable |
| UPDS-WP-007 | Clean-clone recovery | NOT RUN | execute without chat |
| UPDS-WP-008 | Independent backup and restore drill | NOT RUN | create archive/checksum/restore test |
| UPDS-WP-009 | Read-only Document Registry list/get service and API | VERIFIED at 1c06074 | extend only after write-lifecycle contract |
| UPDS-WP-010 | Typed traceability engine | NOT IMPLEMENTED | define relation registry and vertical-slice tests |
| UPDS-WP-011 | Dashboard and project starter | NOT IMPLEMENTED | wait for registry and traceability |
| UPDS-WP-012 | Replace old PR #3 | IMPLEMENTED | PR #3 closed; PR #23 is replacement |
| UPDS-WP-013 | Latest-head CI | VERIFIED at 1c06074 | rerun after subsequent changes |

IMPLEMENTED means files/code exist. VERIFIED requires a passing check and exact SHA. VALIDATED requires acceptance criteria and recorded conditions. NOT RUN and BLOCKED remain explicit.
