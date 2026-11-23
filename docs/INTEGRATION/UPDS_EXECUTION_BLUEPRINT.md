# UPDS Runtime Execution Blueprint
**Document ID:** UPDS-EXEC-0001 | **Status:** PROPOSED — implementation design

## 1. Design objective
Turn the UPDS documentation model into a portable, testable subsystem without duplicating EKTA taxonomy, concept records or graph semantics. Begin with Git-native storage and local APIs; defer database, cloud and multi-user infrastructure until scale and collaboration requirements justify them.

## 2. Bounded modules
1. **Document Registry:** stable IDs, metadata, lifecycle state, revision and source location.
2. **Project Registry:** project identity, scope, owner, lifecycle, constraints and baseline.
3. **Requirements:** requirement statements, rationale, priority, source, acceptance criteria and verification method.
4. **Decision Records:** alternatives, constraints, rationale, consequences, approver and review trigger.
5. **Architecture Catalog:** system/context/component/interface records; reuse EKTA concepts for general engineering entities.
6. **Risk & Change:** risk analysis, issue/change request, impact assessment, approvals and implementation state.
7. **Evidence & Verification:** test cases, runs, raw evidence references, result, environment and traceability.
8. **Lifecycle & Release:** stage gates, baselines, release manifest, deployment/rollback and retirement.
9. **Memory & Handoff:** durable state snapshots and restart instructions.
10. **Validation:** schemas, references, graph integrity, required documents, policy and CI gates.

## 3. Source of truth and storage
Initial canonical store: Git-native structured files (YAML/JSON/Markdown) plus references to native binary artifacts. Do not store large binary files in Git without a deliberate LFS/artifact policy. Runtime indexes are derived and rebuildable; they are never the only copy of canonical data.

Potential later storage adapters may include SQLite for local indexes and external object storage for large evidence, but they require ADRs, migration strategy and offline behavior analysis. No hosted database is assumed.

## 4. Core entity relationships
- Project HAS-DOCUMENT Document
- Project HAS-REQUIREMENT Requirement
- Requirement DERIVED-FROM Source
- Requirement VERIFIED-BY TestCase
- TestCase HAS-RUN TestRun
- TestRun PRODUCES Evidence
- Decision ADDRESSES Requirement
- Decision AFFECTS Component
- Component IMPLEMENTS Concept
- Change MODIFIES Component
- Release CONTAINS Component
- Release SATISFIES Requirement
- Artifact DERIVED-FROM Artifact
- Handoff SNAPSHOTS ProjectState

Relation labels must be registered in the shared typed graph vocabulary before implementation. This list is a candidate set, not a claim that all relations currently exist.

## 5. API boundary proposal
Versioned read/write API should be separated by resource and authorization:
- GET /api/v1/projects and /projects/{project_id}
- GET/POST /api/v1/documents; GET/PATCH /documents/{artifact_id}
- GET/POST /api/v1/requirements; GET/PATCH /requirements/{requirement_id}
- GET/POST /api/v1/decisions; GET/PATCH /decisions/{decision_id}
- GET/POST /api/v1/tests; GET /tests/{test_id}/runs
- GET /api/v1/evidence/{evidence_id}
- GET /api/v1/traceability/{entity_id}
- GET /api/v1/project-state/{project_id}
- POST /api/v1/validate

These are proposed routes only. They must not be treated as existing endpoints or added without schemas, permission model, error contract, idempotency and tests.

## 6. Service contracts
- Validate input before persistence.
- Use optimistic concurrency for updates.
- Preserve immutable revision history.
- Make create operations idempotent when clients provide idempotency keys.
- Return stable error codes and field-level validation errors.
- Never permit arbitrary filesystem paths from API clients.
- Apply project-level authorization before reading or writing.
- Use explicit transactions for multi-entity updates.
- Record actor, timestamp, source and change reason for mutations.

## 7. Status dimensions
Avoid a single overloaded status field. Model independently:
- lifecycle: draft, proposed, active, superseded, archived;
- implementation: not_started, in_progress, implemented;
- verification: not_run, passed, failed, blocked;
- approval: pending, approved, rejected;
- evidence maturity: absent, partial, sufficient, disputed.

Final enumerations must align with existing EKTA/UPDS status conventions and owner governance before schema migration.

## 8. Traceability and impact analysis
A traceability query should answer:
- Which source and stakeholder need created this requirement?
- Which decision resolves it?
- Which architecture/component implements it?
- Which tests verify it?
- Which runs and evidence prove the result?
- Which release includes the implementation?
- What is affected if the requirement, decision or component changes?

Missing edges must be visible as gaps. Never infer satisfaction from a text similarity score.

## 9. Local-first deployment stages
Stage A: Git-native files and CLI validator.  
Stage B: read-only registry API and search.  
Stage C: controlled local write API with backup and audit log.  
Stage D: local dashboard and traceability explorer.  
Stage E: optional collaboration adapters after access/security design.

The current EKTA runtime is read-only. These stages are not yet implemented as UPDS services.

## 10. Minimum vertical slice acceptance
Select one project and one requirement. Create a project record, requirement, decision, component reference, test case, test run and evidence reference. Validate schema and relation integrity. Query the full chain from source requirement to release evidence. Rebuild indexes from a clean clone. Demonstrate that deleting local runtime caches does not lose canonical state.

## 11. Non-goals for first slice
No hosted database, multi-tenant SaaS, workflow automation marketplace, AI auto-approval, arbitrary binary ingestion or full document editor. Defer until a measured need and accepted ADR exist.

## 12. Implementation sequence
1. Inspect existing EKTA schemas, graph model and tests.
2. Define failing tests for ID uniqueness, required fields, valid relations and lifecycle transitions.
3. Extend schemas and validator without changing existing records.
4. Implement repository-backed registry service.
5. Expose read-only API and test response contracts.
6. Add traceability graph and missing-edge reports.
7. Add write operations with audit and concurrency controls.
8. Add dashboard only after API and user flows stabilize.
9. Run clean-clone recovery and archive/restore tests.
