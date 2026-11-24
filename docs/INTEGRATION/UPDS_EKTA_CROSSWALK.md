# UPDS–EKTA Crosswalk and Traceability Model
**Document ID:** UPDS-MAP-0001  
**Status:** PROPOSED

## 1. Core distinction
A reusable engineering concept and a project-controlled artifact are different entities. Example: the general concept "requirements traceability" belongs to EKTA; a specific project's requirements traceability matrix belongs to UPDS and references the EKTA concept.

## 2. Workspace crosswalk
| EKTA workspace | UPDS capabilities | Shared outputs |
|---|---|---|
| DISCOVERY | research brief, feasibility, source register, repository inventory, evidence capture | source records, candidate concepts, research artifacts |
| ENCYCLOPEDIA | taxonomy, document catalog concepts, standards, methods, templates as reusable knowledge | canonical definitions, reusable schemas, provenance |
| DECISION LAB | business/technical trade studies, risk assessment, options, decision approval | ADR/EDR, decision log, comparison matrix |
| EXECUTION LAB | WBS, work packages, implementation, manufacturing, tests, release, operations | procedures, records, test evidence, lessons |

## 3. Cross-domain integration
UPDS applies to all EKTA territories, not only the documentation territory. Examples:
- Software: SRS, API specification, code review, SBOM, test report, release manifest.
- Hardware: HRS, schematic, BOM, PCB revision, calibration, manufacturing acceptance.
- Systems: ConOps, system requirements, ICD, interface verification, safety case.
- AI: model card, dataset card, prompt specification, model evaluation, drift and rollback plan.
- Robotics: system architecture, control model, hazard analysis, firmware and integration tests.
- Operations: runbooks, SLOs, incident reports, maintenance and decommissioning.

## 4. Typed relation vocabulary
Minimum relation set:
- `documents`: a document describes a subject.
- `defines`: establishes a definition or requirement.
- `derived_from`: source/parent requirement or evidence.
- `satisfies`: implementation or design satisfies requirement.
- `implements`: component or artifact realizes design/requirement.
- `verifies`: test or inspection checks conformance.
- `validates`: evidence confirms intended use/need.
- `evidenced_by`: claim or state has supporting evidence.
- `depends_on`: dependency.
- `constrained_by`: constraint relationship.
- `approved_by`: approval authority.
- `supersedes`: controlled replacement, preserving predecessor.
- `impacts`: change impact.
- `contradicts`: conflicting claims or records.
- `references`: non-semantic citation/reference.
- `generalizes_to`: project lesson promoted to reusable EKTA knowledge.

## 5. Traceability chain
```text
Business Objective
  -> Stakeholder Need
  -> System Requirement
  -> Subsystem Requirement
  -> Architecture Decision
  -> Component / Software Module / Hardware Item
  -> Design Specification
  -> Implementation / Build / Manufacturing Lot
  -> Verification Case
  -> Test Run / Inspection / Measurement Evidence
  -> Acceptance / Release
  -> Operational Monitoring / Incident / Maintenance
  -> Lesson Learned
  -> Reusable EKTA Concept / Technique (after review)
```

## 6. Traceability quality rules
- Each controlled requirement has a stable ID, rationale, source, owner, status and acceptance method.
- Each implementation claim links to one or more requirements/design records.
- Each verification claim links to a test case, procedure, environment/configuration and result evidence.
- Each release identifies exact source commit, build inputs, dependencies and artifacts.
- Unverified edges are labeled PROPOSED or RESEARCHED, never silently treated as verified.
- Superseded records remain addressable.
- Orphan nodes, broken references, circular derivation and contradictory baselines are detected or explicitly waived.

## 7. ID namespaces
Keep EKTA knowledge IDs and UPDS project-artifact IDs distinct:
- EKTA existing families: EKTA-CON, EKTA-TEC, EKTA-ARC, EKTA-CMP, EKTA-STD, EKTA-TOL, EKTA-SRC, EKTA-DEC, EKTA-WFL, EKTA-TST.
- UPDS proposed families: UPDS-DOC, UPDS-REQ, UPDS-ADR, UPDS-RSK, UPDS-ISS, UPDS-CHG, UPDS-TST, UPDS-EVD, UPDS-REL, UPDS-MEM, UPDS-BASE, UPDS-WP.
- Project-specific IDs should be namespaced by project: `<PROJECT>-REQ-0001`, etc. Never use an unqualified global numeric ID.
IDs are immutable and never recycled. A rename or move changes a label/path, not identity.

## 8. Status model
Keep EKTA's current statuses intact. UPDS may use document lifecycle statuses:
`DRAFT, PROPOSED, IN_REVIEW, APPROVED, BASELINED, IMPLEMENTED, VERIFIED, VALIDATED, SUPERSEDED, DEPRECATED, BLOCKED, NOT_RUN, ARCHIVED`.
Statuses are not a single linear enum: implementation, verification and validation may be separate dimensions. The schema should model lifecycle_state, implementation_state, verification_state and validation_state separately where needed.

## 9. Evidence object minimum
- evidence_id, title, evidence_type, source_uri/path, captured_at, captured_by;
- subject_ids, requirement_ids, test_case_id, configuration_id;
- environment, tool/version, procedure/version;
- result, limitations, integrity_hash (when practical), reviewer, status.
Evidence is immutable once baselined; corrections create a superseding record.

## 10. Reconciliation and migration
Do not duplicate EKTA concepts into UPDS. Link the UPDS artifact to the EKTA canonical concept. For existing EKTA documents, add UPDS metadata only when they genuinely behave as controlled project artifacts; otherwise retain them as EKTA knowledge/documentation. Record every migration decision in a migration ledger.
