# ADR-0001: Repository license and content policy

- Status: Proposed
- Date: 2026-11-23
- Decision owner: Project maintainer

## Context
EKTA is public and will contain documentation, schemas, tooling, and references. No license has been selected. Third-party projects and standards have different reuse rights.

## Decision drivers
Reuse clarity, commercial flexibility, contributor expectations, attribution, patent risk, and upstream compatibility.

## Options
1. One license for all repository content.
2. Separate documentation and software licenses.
3. Keep licensing undecided temporarily.

## Proposed decision
Keep licensing explicitly undecided during bootstrap. Do not imply public visibility grants reuse rights. Before a stable release, evaluate separate documentation and software licenses and record the decision in a superseding ADR.

## Consequences
No downstream reuse permission should be assumed. Third-party assets must be linked or used only under their own terms. License selection is a release gate.

## Verification
Confirm an approved license file and updated policy exist only after maintainer approval.
