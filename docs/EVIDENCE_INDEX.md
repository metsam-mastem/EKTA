# Evidence Index

| Evidence ID | Claim / artifact | Location | Status |
|---|---|---|---|
| EKTA-EVD-0001 | Existing EKTA repository tree inspected | GitHub tree on 2026-11-23 | VERIFIED (inspection only) |
| EKTA-EVD-0002 | Existing runtime package and dependencies inspected | pyproject.toml | VERIFIED (file inspection only) |
| EKTA-EVD-0003 | Existing CI validation steps inspected | .github/workflows/validate.yml | VERIFIED (workflow definition only; not execution) |
| UPDS-EVD-0001 | UPDS architecture/catalog files created on integration branch | docs/INTEGRATION/ | IMPLEMENTED (branch files present) |
| UPDS-EVD-0002 | Integration branch automated tests | NOT RUN | NOT_RUN |

A file's existence is evidence of a repository change, not evidence that its behavior is correct.

| UPDS-EVD-0003 | Full EKTA CI validation including UPDS schema validator and unit tests | [GitHub Actions run 45124354424](https://github.com/metsam-mastem/EKTA/actions/runs/45124354424), commit d7b1fed9e52ba10a792ab18bbfd7fae6dc44e781 | VERIFIED — SUCCESS |
