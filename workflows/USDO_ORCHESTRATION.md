# USDO Development Orchestration

**Workstream:** EKTA / USDO foundation  
**Branch:** knowledge/usdo-ontology-foundation  
**State:** ACTIVE PLAN — no autonomous background execution is implied

## Objective

Develop the USDO foundation in parallel workstreams while keeping one canonical repository, one shared data contract, explicit dependencies, and evidence-backed completion states.

## Parallel workstreams

| ID | Workstream | Scope | Deliverables | Depends on |
|---|---|---|---|---|
| WS-01 | Ontology and terminology | Definitions, facet boundaries, controlled terms, ambiguity register | Facet registry, glossary, concept records | Initial design |
| WS-02 | Schema and quality engineering | JSON Schema, YAML contracts, validators, unit tests, CI | Validated contracts and CI evidence | WS-01 |
| WS-03 | Domain exemplars | Computing, software, electronics, control, networking, mechanical, organizational examples | Domain records and cross-domain comparison matrix | WS-01, WS-02 |
| WS-04 | Standards and open-source research | Standards, formal models, open-source tools, license and version review | Source register, evidence notes, adoption decisions | WS-01 |
| WS-05 | Graph and runtime integration | Entity IDs, typed relations, facet projections, search and graph export | Runtime integration proposal and tested graph projection | WS-01, WS-02, WS-03 |
| WS-06 | Visualization and workbench | Multi-view maps, matrices, layer views, topology and state views | UI specification, interaction model, acceptance tests | WS-01, WS-05 |

## Parallel execution policy

- WS-01 and WS-02 proceed together, with schema changes reviewed against semantic definitions.
- WS-03 and WS-04 proceed in parallel after the initial contract stabilizes.
- WS-05 starts only after identifiers, relation semantics, and at least three domain examples are reviewed.
- WS-06 starts after a stable graph/API contract exists; do not build a visualization against unstable data shapes.
- Cross-workstream changes are integrated through small pull requests or isolated commits. Do not create competing canonical registries.
- Any change to approved EKTA territory IDs, existing layer IDs, or base relation predicates requires explicit review and, where material, an ADR.

## Execution cycle

Each work item follows:

1. Define the question, scope, and acceptance criteria.
2. Research primary sources and inspect relevant open-source implementations.
3. Record claims separately from assumptions and proposals.
4. Implement the smallest testable change.
5. Run schema, unit, integration, documentation, and link checks relevant to the change.
6. Review evidence and deviations.
7. Correct and retest.
8. Publish a handoff with changed paths, commit, test evidence, unresolved risks, and next dependency.

## Status vocabulary

- PROPOSED: design suggestion, not yet accepted.
- RESEARCHED: sources inspected; conclusions still require review.
- VERIFIED: claim checked against cited evidence in a defined scope.
- IMPLEMENTED: code or documentation exists in the repository.
- VALIDATED: stated acceptance criteria passed with recorded evidence.
- NOT_RUN: required check has not run.
- BLOCKED: dependency or permission prevents progress.
- DEPRECATED: retained for history but superseded.

A successful CI run validates only the checks actually executed. It does not prove conceptual completeness, external standards conformance, or production readiness.

## Current baseline

- USDO facet registry: implemented in this branch.
- USDO JSON Schema: implemented in this branch.
- Persian architecture documentation: implemented in this branch.
- Relation matrix, template, and generic CPU example: implemented in this branch.
- Local validator and tests: implemented in this branch.
- CI integration: implemented in this branch; CI evidence is tracked on PR #13.
- Runtime API, graph projection, UI, ontology reasoning, and domain-wide coverage: not implemented by this foundation.

## Immediate next sequence

1. Review PR #13 and its CI result.
2. Resolve reviewer feedback and freeze the v0.1 contract.
3. Add individual concept records for Dimension, Scope, Scale, Layer, Topology, Circuit, Relation, Flow, Process, State, and Evaluation.
4. Add network, feedback-control, and software-architecture examples.
5. Review standards and open-source model/tool options before selecting any runtime dependency.
6. Design a typed graph projection and add tests for relation direction, target resolution, provenance, and facet boundaries.
7. Draft the workbench views only after the graph/API contract is stable.

## Operational limitation

This document establishes the orchestration protocol and dependency graph. It does not create a continuously running agent or guarantee unattended work after a chat session ends. Work proceeds through explicit commits, pull requests, CI runs, and reviewable handoffs.
