# Evidence Index

| Evidence ID | Claim / artifact | Evidence reference | Status |
|---|---|---|---|
| EKTA-EVD-0001 | Main baseline used for clean port | https://github.com/metsam-mastem/EKTA/commit/7ea271e00ef2cb010c17bdaa553e1f27645f12ca | VERIFIED — commit observed |
| EKTA-EVD-0002 | Persian-first user docs exist on main | docs/USER_DOCUMENTATION_INDEX.md | VERIFIED — file inspected |
| UPDS-EVD-0001 | Old branch diverged 57 ahead / 35 behind | GitHub compare main...integration/upds-documentation-architecture | VERIFIED — 2026-11-24 |
| UPDS-EVD-0002 | Old PR #3 closed without merge | https://github.com/metsam-mastem/EKTA/pull/3 | VERIFIED |
| UPDS-EVD-0003 | Clean replacement PR and branch | https://github.com/metsam-mastem/EKTA/pull/23 | IMPLEMENTED; clean branch based on main |
| UPDS-EVD-0004 | Schema, sample record, validator and base tests | schemas/upds-document.schema.json; tools/; tests/; upds/ | VERIFIED by run 45305319405 |
| UPDS-EVD-0005 | Read-only registry service/API and tests | runtime/ekta_runtime/upds_registry.py; runtime/ekta_runtime/api.py; tests/test_upds_registry.py | VERIFIED by run 45305319405 |
| UPDS-EVD-0006 | Continuity validator and tests | tools/validate_continuity.py; tests/test_continuity.py | VERIFIED by run 45305319405 |
| UPDS-EVD-0007 | Latest full CI passed | https://github.com/metsam-mastem/EKTA/actions/runs/45305319405; SHA 8453a2d179490969a5b2262c8d8e34ba957d3d5c | VERIFIED for exact SHA |
| UPDS-EVD-0008 | Earlier registry CI pass | https://github.com/metsam-mastem/EKTA/actions/runs/45304968576; SHA 1c06074a8d31b87602b4426cb70640a8b26571aa | VERIFIED for exact SHA |
| UPDS-EVD-0009 | Continuity validator initial failure and fix | https://github.com/metsam-mastem/EKTA/actions/runs/45305226654 | FAIL diagnosed: escaped newlines in YAML; fixed and superseded |
| UPDS-EVD-0010 | Conversation archive, manifest, recovery, agent onboarding and orchestration | docs/PROJECT_CONTINUITY/ | IMPLEMENTED as structured summary, not raw transcript |
| UPDS-EVD-0011 | Clean-clone human recovery without chat | docs/PROJECT_CONTINUITY/RECOVERY_RUNBOOK.md | NOT RUN |
| UPDS-EVD-0012 | Independent backup restore/checksum | not yet executed | NOT RUN |
| UPDS-EVD-0013 | Full traceability, dashboard and project starter | execution blueprint/roadmap | NOT IMPLEMENTED |

A file proves existence, not behavior. CI evidence applies only to the exact commit tested.
