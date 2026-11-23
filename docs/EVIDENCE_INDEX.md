# Evidence Index

| Evidence ID | Claim / artifact | Location | Status |
|---|---|---|---|
| EKTA-EVD-0001 | Existing EKTA repository tree inspected | GitHub tree, 2026-11-23 | VERIFIED (inspection only) |
| EKTA-EVD-0002 | Runtime package and dependencies inspected | pyproject.toml | VERIFIED (file inspection only) |
| EKTA-EVD-0003 | CI validation steps inspected | .github/workflows/validate.yml | VERIFIED (workflow definition only) |
| UPDS-EVD-0001 | UPDS architecture/catalog committed to integration branch | docs/INTEGRATION/ | IMPLEMENTED |
| UPDS-EVD-0002 | Base schema, sample fixture, validator and tests present | schemas/, tools/, upds/, tests/ | IMPLEMENTED |
| UPDS-EVD-0003 | CI run 45124354424 passed on commit d7b1fed9e52ba10a792ab18bbfd7fae6dc44e781 | https://github.com/metsam-mastem/EKTA/actions/runs/45124354424 | VERIFIED for that exact commit only |
| UPDS-EVD-0004 | User guide set committed | docs/USER_GUIDE/ | IMPLEMENTED; platform execution NOT RUN |
| UPDS-EVD-0005 | Clean-clone recovery without chat | docs/USER_GUIDE/RECOVERY_AND_CONTINUITY.md | NOT RUN |
| UPDS-EVD-0006 | Latest branch HEAD CI after user guide commits | GitHub Actions | NOT VERIFIED |

A file's existence proves that a repository change exists; it does not prove behavior, correctness or usability. Evidence must identify the exact commit, command/test, result and limitations.
