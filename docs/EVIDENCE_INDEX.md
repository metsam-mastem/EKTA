# Evidence Index

| Evidence ID | Claim / artifact | Location | Status |
|---|---|---|---|
| EKTA-EVD-0001 | Repository tree inspected | GitHub tree, 2026-11-23 | VERIFIED (inspection only) |
| EKTA-EVD-0002 | Runtime package/dependencies inspected | pyproject.toml | VERIFIED (file inspection only) |
| EKTA-EVD-0003 | CI workflow definition inspected | .github/workflows/validate.yml | VERIFIED (definition only) |
| UPDS-EVD-0001 | UPDS architecture/catalog committed to integration branch | docs/INTEGRATION/ | IMPLEMENTED |
| UPDS-EVD-0002 | Base schema, sample, validator and tests present | schemas/, tools/, upds/, tests/ | IMPLEMENTED |
| UPDS-EVD-0003 | CI run 45124354424 passed at d7b1fed9e52ba10a792ab18bbfd7fae6dc44e781 | https://github.com/metsam-mastem/EKTA/actions/runs/45124354424 | VERIFIED for exact SHA only |
| UPDS-EVD-0004 | User documentation merged to main by PR #4 | https://github.com/metsam-mastem/EKTA/commit/82c2e8a58f7c8449a440822183d30a8fdf81a73f | IMPLEMENTED; validation details recorded in continuity handoff |
| UPDS-EVD-0005 | Supplemental docs/USER_GUIDE in integration branch | docs/USER_GUIDE/ | IMPLEMENTED; platform tests NOT RUN |
| UPDS-EVD-0006 | Input/artifact model and runtime execution blueprint | docs/INTEGRATION/ | IMPLEMENTED as design only |
| UPDS-EVD-0007 | Clean-clone recovery without chat | docs/USER_GUIDE/RECOVERY_AND_CONTINUITY.md | NOT RUN |
| UPDS-EVD-0008 | Latest integration branch HEAD CI | latest known SHA 243f27b82b83f721174bec97085fc5abb5cb7001 | NOT VERIFIED |

File existence proves a repository change, not behavior, correctness or usability. Every verification claim must name exact commit, command, result and limitations.
