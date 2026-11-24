# MUA Implementation Plan

## Operating model

Work is divided into parallel workstreams with explicit interface boundaries. Parallel work does not mean parallel writes to shared contracts. The schema and identifier registry remain centrally governed.

| Workstream | Focus | First output | Dependency |
|---|---|---|---|
| A — Ontology & taxonomy | Mathematical kinds and controlled terms | Kind registry | UMO contract |
| B — UMO & graph | Identity, schema, references, lifecycle | Schema, validator, graph tests | Canonical ID rules |
| C — Coordinate & projection | Frames, axes, units, transforms | Coordinate contract and test vectors | UMO structure |
| D — Visual grammar | Semantic-to-visual mapping and accessibility | Visual encoding registry | Representation contract |
| E — Computation adapters | Symbolic, numerical, proof capabilities | Adapter interface and reproducibility record | UMO behavior |
| F — Workspace | Authoring, inspection, history, import/export | One-entity vertical slice | Stable contracts |
| G — Evidence & QA | Sources, fixtures, validation, CI | Acceptance matrix and evidence log | All streams |

## Orchestration protocol

1. Read EKTA governance, current schemas, taxonomy registries, tests, and runtime boundaries before editing.
2. Maintain a single canonical integration branch; avoid concurrent writes to the same branch ref.
3. Parallelize research and isolated drafts, not competing schema edits.
4. Every workstream publishes assumptions, changed paths, tests, evidence, unresolved risks, and next dependency.
5. Integrate through small commits or pull requests; run complete repository validation after integration.
6. Use NOT_RUN, BLOCKED, FAIL, and PASS precisely. Generated source is not proof of a passing test.
7. Do not merge into main without review and explicit maintainer decision.

## Current foundation slice

- schemas/mathematical-object.schema.json
- schemas/coordinate-frame.schema.json
- runtime/ekta_runtime/mathematics.py
- tests/test_mathematics.py
- examples/mathematical-universe/quadratic-function.umo.json

The implementation is intentionally small and standard-library-only. It establishes deterministic structural checks while leaving formal mathematical verification to specialized engines.

## Next acceptance gates

- [ ] Add CI execution for MUA tests and schema meta-validation.
- [ ] Validate the example against JSON Schema in a test.
- [ ] Add relation-predicate registry and target-kind constraints.
- [ ] Add UMO Markdown/YAML authoring template.
- [ ] Define coordinate transformation contracts and dimensional-analysis policy.
- [ ] Define visual grammar semantics and accessibility tests.
- [ ] Implement a minimal inspect/edit/render/export workspace slice.
- [ ] Evaluate OpenMath and MathML adapters against concrete test cases.
