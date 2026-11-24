# Evidence Index

| Evidence ID | Claim / artifact | Evidence reference | Status |
|---|---|---|---|
| EKTA-EVD-0001 | Main baseline used for clean port | https://github.com/metsam-mastem/EKTA/commit/7ea271e00ef2cb010c17bdaa553e1f27645f12ca | VERIFIED — commit observed |
| EKTA-EVD-0002 | Persian-first user docs exist on main | docs/USER_DOCUMENTATION_INDEX.md | VERIFIED — file inspected |
| UPDS-EVD-0001 | Old branch diverged 57 ahead / 35 behind | GitHub compare main...integration/upds-documentation-architecture | VERIFIED — 2026-11-24 |
| UPDS-EVD-0002 | Old PR #3 closed without merge | https://github.com/metsam-mastem/EKTA/pull/3 | VERIFIED |
| UPDS-EVD-0003 | Clean replacement PR and branch | https://github.com/metsam-mastem/EKTA/pull/23 | IMPLEMENTED; latest compare 58 ahead / 0 behind |
| UPDS-EVD-0004 | Schema, sample record, validator and base tests | schemas/upds-document.schema.json; tools/; tests/; upds/ | VERIFIED at fdd995f via CI run 45304714331 |
| UPDS-EVD-0005 | CI run 45304714331 passed | https://github.com/metsam-mastem/EKTA/actions/runs/45304714331; SHA fdd995f173c7d51a777f9e841172c648b4af3cad | VERIFIED for exact SHA |
| UPDS-EVD-0006 | Read-only registry service/API and tests | runtime/ekta_runtime/upds_registry.py; runtime/ekta_runtime/api.py; tests/test_upds_registry.py | IMPLEMENTED; latest CI pending |
| UPDS-EVD-0007 | Earlier full CI run passed | https://github.com/metsam-mastem/EKTA/actions/runs/45304523297; SHA 11ac9b7689b366299e7856a814cae289c63b4e24 | VERIFIED for exact SHA |
| UPDS-EVD-0008 | Conversation archive, manifest, recovery, agent onboarding and orchestration | docs/PROJECT_CONTINUITY/ | IMPLEMENTED as structured summary, not raw transcript |
| UPDS-EVD-0009 | Latest registry implementation CI | GitHub Actions run 45304839153 queued at previous check | NOT VERIFIED |
| UPDS-EVD-0010 | Clean-clone recovery without chat | docs/PROJECT_CONTINUITY/RECOVERY_RUNBOOK.md | NOT RUN |
| UPDS-EVD-0011 | Independent backup restore/checksum | not yet executed | NOT RUN |
| UPDS-EVD-0012 | Full traceability, dashboard and project starter | execution blueprint/roadmap | NOT IMPLEMENTED |

A file proves existence, not behavior. CI evidence applies only to the exact commit tested.
