# EKTA Project State
**Status:** PROPOSED INTEGRATION BRANCH — 2026-11-23

## Canonical identity
- Project: Engineering Knowledge & Techniques Atlas (EKTA)
- Repository: https://github.com/metsam-mastem/EKTA
- Default branch: main
- Integration branch: integration/upds-documentation-architecture
- Current branch purpose: additive UPDS architecture and document-universe integration.

## Verified repository baseline
- Python package: ekta-runtime 0.2.0; Python >=3.11.
- Existing runtime, browser explorer, taxonomy, schemas, templates, tests and CI are present in the inspected tree.
- Existing documentation includes project charter, master handoff, context continuity, lifecycle, knowledge architecture, governance, quality/evidence and implementation plan.
- Existing CI workflow runs documentation validation, unittest discovery, frontend validation and graph export.
- Repository license remains undecided (see LICENSE-STATUS.md).

## Integration state
- UPDS–EKTA integration decision: PROPOSED.
- UPDS system architecture: PROPOSED.
- Universal document catalog: added on integration branch.
- Crosswalk, memory independence, template standard and roadmap: added on integration branch.
- Runtime integration, UPDS schemas, validators, UI and graph nodes/edges: NOT IMPLEMENTED by this documentation-only change.
- Tests/CI for this branch: NOT RUN in this environment.

## Next actions
1. Review the proposed integration ADR and approve/revise it.
2. Review catalog applicability and ID namespaces.
3. Add machine-readable UPDS schemas and sample fixtures.
4. Extend validators with tests before implementation.
5. Reconcile README, repository map and master handoff.
6. Run existing CI and record exact results.
