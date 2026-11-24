# ECPS Orchestration Plan 0.1

**Status:** ACTIVE PLAN · **Snapshot:** 2026-11-24

## 1. Execution rule

Develop independent contracts and adapters in parallel only where their file/API boundaries are stable. Do not edit the four source workstream branches from ECPS. Every merge candidate must be tested against pinned source revisions and must include evidence. No background or unattended execution is implied; orchestration is represented by explicit branches, pull requests, CI runs and handoffs.

## 2. Workstreams

| ID | Workstream | Parallel output | Dependency / gate |
|---|---|---|---|
| OR-00 | Source contract audit | Exact schema/code/commit inventory for UMSF, MUA, VEL, VES | Complete for 0.1; refresh after upstream merge |
| OR-01 | Coordinate semantics | Registry and non-conflation rules for semantic, geometric, board, diagram and temporal spaces | UMSF + MUA + VES + VEL contracts reviewed |
| OR-02 | Projection manifest | Versioned manifest schema, stable references, source revisions | OR-00 and OR-01 |
| OR-03 | Projection compiler | Deterministic renderer-neutral view plan | OR-02; no source mutation |
| OR-04 | Workstream adapters | Read-only UMSF/MUA/VEL/VES import adapters and loss reports | Source PRs merged or pinned; adapter-specific fixtures |
| OR-05 | View synchronization | Shared selection/identity across 2D, graph, matrix, timeline and 3D views | OR-04; stable cross-model identity policy |
| OR-06 | Verification | Schema, semantic, adapter, round-trip and regression tests | Each adapter and projection gate |
| OR-07 | Workbench integration | ECPS projection plans consumed by VES without taking over its board model | VES API and mutation policy reviewed |

## 3. Dependency graph

```text
Source audit (OR-00)
        |
Coordinate semantics (OR-01)
        |
Projection manifest (OR-02)
        |
Projection compiler (OR-03)
        +----------------------------------+
       |                           |
Read-only adapters (OR-04)     Test fixtures / conformance
        |                           |
Cross-view synchronization (OR-05)
        |
Workbench integration (OR-07)
        |
Release verification (OR-06)
```

## 4. Current evidence

- Four upstream draft PRs inspected: UMSF #11, VEL #10, MUA #19, VES #20.
- Coordinate ownership and non-conflation matrix documented.
- Projection manifest schema and reference example created.
- Python contract validator and renderer-neutral plan compiler created.
- Local test suite: 10/10 PASS.
- Example manifest CLI validation: PASS.
- Full EKTA CI on the ECPS branch: NOT RUN at the time of this plan.
- Actual import/export adapters and graphical renderers: NOT IMPLEMENTED.

## 5. TEIR gate

For each workstream:

1. Test: run schema, unit, integration and conformance fixtures.
2. Evaluate: inspect output and source revision compatibility.
3. Identify deviation: record mismatches, missing fields and lossy mappings.
4. Correct: update adapter/contract without rewriting source authority.
5. Retest: rerun the exact failed and regression suites.
6. Re-evaluate: promote status only with CI and review evidence.

Status vocabulary: PASS / FAIL / NOT RUN / BLOCKED. A green unit suite does not imply adapter compatibility, physical validity or production readiness.

## 6. Immediate next actions

1. Open an ECPS draft PR against the latest EKTA `main` snapshot.
2. Wait for EKTA CI and address any repo-level failures.
3. Reconcile UMSF and VEL PR bases against current `main` before their merge.
4. After the four upstream contracts are reviewed/merged, pin their merged commits and refresh the manifest fixture.
5. Implement one read-only adapter at a time, starting with UMSF semantic graph → projection plan.
6. Add MUA frame references, then VEL topology, then VES board view-state.
7. Do not claim synchronized editing or round-trip compatibility until the dedicated tests pass.
