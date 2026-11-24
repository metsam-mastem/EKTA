# Evidence Index

| Evidence ID | Claim / artifact | Evidence reference | Status |
|---|---|---|---|
| EKTA-EVD-0001 | Main baseline used for clean port | https://github.com/metsam-mastem/EKTA/commit/7ea271e00ef2cb010c17bdaa553e1f27645f12ca | VERIFIED — commit observed |
| EKTA-EVD-0002 | Persian-first user docs exist on main | docs/USER_DOCUMENTATION_INDEX.md | VERIFIED — file inspected |
| UPDS-EVD-0001 | Old branch diverged 57 ahead / 35 behind | GitHub compare main...integration/upds-documentation-architecture | VERIFIED — captured 2026-11-24 |
| UPDS-EVD-0002 | Historical old-branch CI passed on exact SHA | https://github.com/metsam-mastem/EKTA/actions/runs/45124354424 | VERIFIED for d7b1fed9e52ba10a792ab18bbfd7fae6dc44e781 only |
| UPDS-EVD-0003 | Clean continuation branch and replacement PR | https://github.com/metsam-mastem/EKTA/pull/23 | IMPLEMENTED; branch compare 48 ahead / 0 behind at last check |
| UPDS-EVD-0004 | Schema, sample record, validator and tests | schemas/upds-document.schema.json; tools/; tests/; upds/ | IMPLEMENTED |
| UPDS-EVD-0005 | CI run 45304523297 passed | https://github.com/metsam-mastem/EKTA/actions/runs/45304523297; commit 11ac9b7689b366299e7856a814cae289c63b4e24 | VERIFIED on exact SHA; all listed steps success |
| UPDS-EVD-0006 | Chat context archive, manifest, recovery and agent onboarding | docs/PROJECT_CONTINUITY/ | IMPLEMENTED as structured summary, not raw transcript |
| UPDS-EVD-0007 | Old PR #3 closed and superseded by PR #23 | https://github.com/metsam-mastem/EKTA/pull/3 | VERIFIED — closed, not merged |
| UPDS-EVD-0008 | Latest PR #23 head CI | GitHub Actions | NOT VERIFIED at snapshot |
| UPDS-EVD-0009 | Clean-clone recovery without chat | docs/PROJECT_CONTINUITY/RECOVERY_RUNBOOK.md | NOT RUN |
| UPDS-EVD-0010 | Independent backup restore/checksum | not yet executed | NOT RUN |
| UPDS-EVD-0011 | Registry/API and full traceability | execution blueprint/roadmap | NOT IMPLEMENTED |

A file proves its existence, not behavior. CI evidence applies only to the exact commit tested. Do not transfer historical pass results to later commits.
