# Evidence Index

| Evidence ID | Claim / artifact | Evidence reference | Status |
|---|---|---|---|
| EKTA-EVD-0001 | EKTA main baseline at start of clean port | https://github.com/metsam-mastem/EKTA/commit/7ea271e00ef2cb010c17bdaa553e1f27645f12ca | VERIFIED — commit observed |
| EKTA-EVD-0002 | User documentation index exists on main | docs/USER_DOCUMENTATION_INDEX.md | VERIFIED — file inspected |
| UPDS-EVD-0001 | Old UPDS integration branch diverged from main | compare main...integration/upds-documentation-architecture: 57 ahead, 35 behind | VERIFIED — compare result at 2026-11-24 |
| UPDS-EVD-0002 | Old CI run passed on exact historical SHA | https://github.com/metsam-mastem/EKTA/actions/runs/45124354424; SHA d7b1fed9e52ba10a792ab18bbfd7fae6dc44e781 | VERIFIED for that SHA only |
| UPDS-EVD-0003 | UPDS architecture/schema/validator/test files ported to clean branch | integration/upds-independent-continuity | IMPLEMENTED; latest CI pending |
| UPDS-EVD-0004 | Chat session context archive, manifest, recovery and agent onboarding added | docs/PROJECT_CONTINUITY/ | IMPLEMENTED as structured docs; not a raw transcript |
| UPDS-EVD-0005 | CI gate for UPDS validator added to clean branch | .github/workflows/validate.yml | IMPLEMENTED; workflow run pending |
| UPDS-EVD-0006 | Clean-clone recovery without chat | docs/PROJECT_CONTINUITY/RECOVERY_RUNBOOK.md | NOT RUN |
| UPDS-EVD-0007 | Independent backup restore and checksum | not yet executed | NOT RUN |
| UPDS-EVD-0008 | Registry/API and graph traceability | roadmap and execution blueprint | NOT IMPLEMENTED |

A file proves its existence, not behavior. A CI result proves only the exact commit and checks run. Do not transfer old CI evidence to new commits.
