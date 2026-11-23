# EKTA Project State
**Status:** UPDS integration proposal branch — documentation and initial validation foundation  
**Last state update:** 2026-11-23

## Canonical identity
- Project: Engineering Knowledge & Techniques Atlas (EKTA)
- Repository: https://github.com/metsam-mastem/EKTA
- Default branch: main
- UPDS integration branch: integration/upds-documentation-architecture
- UPDS proposal PR: https://github.com/metsam-mastem/EKTA/pull/3
- Separate Persian-first user documentation PR #4 was merged to main at 82c2e8a58f7c8449a440822183d30a8fdf81a73f.
- License remains undecided; do not add or imply a license.

## Product boundary
EKTA is the engineering knowledge atlas and typed knowledge environment. UPDS is a bounded, separable, cross-cutting subsystem for project documentation, lifecycle, requirements, decisions, evidence, traceability and durable project memory. Integration ADR remains PROPOSED pending owner review.

## Integration branch contents
- UPDS architecture, document universe, crosswalk, template standard, memory protocol, input/artifact model, runtime execution blueprint and roadmap.
- State, decision, active-work, issue, constraint, evidence and handoff registers.
- Base JSON Schema, validation primitives, repository validator, sample record and unit tests.
- Supplemental docs/USER_GUIDE set.
- Earlier README and CI changes.

## Verification boundaries
- Base schema, sample fixture and validator code: IMPLEMENTED.
- CI run 45124354424 passed at commit d7b1fed9e52ba10a792ab18bbfd7fae6dc44e781; evidence applies only to that SHA.
- User docs on main: IMPLEMENTED by PR #4; its handoff reports docs validation, 29 tests, frontend checks and graph export passing on PR head d1463eefe9e7ceb17c8fdf39b862a2a10c04e12c. Post-merge CI is a separate check.
- Supplemental user docs in this branch: IMPLEMENTED as files; platform execution NOT RUN.
- UPDS registry/API, typed traceability engine, graph integration, dashboard and project starter: NOT IMPLEMENTED.
- Clean-clone recovery and independent backup restore: NOT RUN.
- Latest integration branch HEAD CI: NOT VERIFIED.

## Safety constraints
Do not merge PR #3 or change main without explicit owner approval. Do not change license, introduce hosted dependencies, delete/rename canonical content or alter EKTA taxonomy without approval. Preserve IDs and history. Use TDD for behavior changes.

## Next safe actions
1. Refresh PR #3 state and latest branch HEAD.
2. Consolidate supplemental user docs with the Persian-first docs already on main.
3. Verify latest-HEAD CI.
4. Run clean-clone recovery without chat.
5. Add automated register/link checks.
6. Implement registry service/API with TDD.
7. Implement traceability, dashboard and starter generator in separate vertical slices.
8. Obtain owner review of integration ADR.

Chat history is non-canonical. The repository and independently tested backups must be sufficient to resume.
