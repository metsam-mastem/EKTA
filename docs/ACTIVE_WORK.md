# Active Work Register
**Baseline:** integration/upds-documentation-architecture  
**Updated:** 2026-11-23

| Work ID | Work package | Status | Evidence / next action |
|---|---|---|---|
| UPDS-WP-001 | Additive integration architecture and catalog | IMPLEMENTED | docs/INTEGRATION; review proposed ADR |
| UPDS-WP-002 | Owner review of integration decision | BLOCKED | Owner must approve/revise EKTA-ADR-0003 |
| UPDS-WP-003 | Machine-readable artifact schema and sample record | IMPLEMENTED | schema + fixture; prior CI pass on recorded SHA |
| UPDS-WP-004 | Document record validator and unit tests | IMPLEMENTED | validator + tests + CI step; latest HEAD still requires CI verification |
| UPDS-WP-005 | Runtime document registry/API | NOT RUN | define contracts and failing tests, then implement |
| UPDS-WP-006 | Full typed graph traceability | NOT RUN | requirements → decisions → components → tests → evidence |
| UPDS-WP-007 | User docs: overview/setup/install/manual/admin | IMPLEMENTED | docs/USER_GUIDE; platform execution tests NOT RUN |
| UPDS-WP-008 | Chat-independent recovery protocol | IMPLEMENTED (design/docs) | clean-clone recovery drill NOT RUN |
| UPDS-WP-009 | Automated recovery and docs completeness checks | NOT RUN | define invariants and add tests |
| UPDS-WP-010 | Project starter generator and completeness dashboard | NOT RUN | defer until registry/schema stable |
| UPDS-WP-011 | Owner architecture review and PR disposition | BLOCKED | no merge without explicit owner approval |

## Status rules
IMPLEMENTED means files/code exist. VERIFIED requires a specific passing check and commit SHA. VALIDATED requires acceptance criteria and recorded test conditions. NOT RUN and BLOCKED must remain explicit.

No item is marked VERIFIED solely because a file exists.
