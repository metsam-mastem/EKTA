# UPDS Document Template and Metadata Standard
**Document ID:** UPDS-STD-0001  
**Status:** PROPOSED

## 1. Universal metadata
Every controlled artifact should carry the following metadata, using YAML front matter for Markdown when practical:

```yaml
---
id: PROJECT-REQ-0001
title: Example requirement
artifact_type: requirement
family: requirements
level: L2
domain: systems
project_id: PROJECT
status: PROPOSED
version: 0.1.0
owner: ""
author: ""
reviewer: ""
approver: ""
created: YYYY-MM-DD
updated: YYYY-MM-DD
classification: internal
applicability: REQUIRED
source_ids: []
parent_ids: []
related_ids: []
satisfies_ids: []
implemented_by_ids: []
verified_by_ids: []
evidence_ids: []
supersedes: []
---
```

## 2. Required body sections
1. Purpose
2. Scope and exclusions
3. Context and rationale
4. Definitions
5. Inputs and source references
6. Requirements/content/specification
7. Interfaces and dependencies
8. Constraints and assumptions
9. Risks and failure considerations
10. Acceptance / review criteria
11. Verification and validation method
12. Related artifacts and traceability
13. Change history
14. Open questions and next actions

Not every section applies to every artifact. Templates may tailor sections but must explicitly retain relevant safety, evidence, traceability and ownership fields.

## 3. Artifact-specific templates
- Project charter: mission, sponsor/owner, objectives, scope, exclusions, outcomes, authority, constraints, high-level risks, approval.
- Requirements: unique statement, rationale, source, fit criterion, verification method, priority, owner, allocation, dependencies, status.
- Architecture decision: context, drivers, options, decision, rationale, consequences, rejected alternatives, evidence, review trigger.
- Architecture description: context, stakeholders, concerns, viewpoints, views, interfaces, constraints, rationale, quality attributes.
- Test case: ID, objective, requirement links, preconditions, configuration, steps, expected result, actual result, verdict, evidence.
- Test report: scope, environment, build/configuration, procedures, summary, deviations, defects, evidence, conclusion.
- Risk: cause-event-effect, likelihood, impact, exposure, owner, mitigation, trigger, residual risk, review date.
- Change request: reason, baseline, requested change, impact, alternatives, risk, approval, implementation and verification.
- Release manifest: version, source commit, build inputs, dependency/SBOM references, artifacts, checksums, test evidence, known issues, rollback.
- Session handoff: baseline commit, completed work with evidence, current state, blockers, decisions, changed paths, exact next actions.
- Hardware BOM: reference designator, manufacturer, MPN, description, quantity, footprint/package, lifecycle, approved alternatives, supplier, datasheet and revision.
- Software component: module ID, purpose, public interfaces, dependencies, data contracts, failure modes, security properties, tests and ownership.

## 4. Versioning
- Use semantic versioning for reusable schemas/templates and software packages where compatible.
- Document revisions may use major.minor.patch: major for incompatible baseline changes, minor for additive approved content, patch for editorial corrections.
- Never rewrite a released baseline in place; issue a new revision and retain the old one.
- Git commit history is necessary but does not replace document-level revision metadata for externally controlled deliverables.

## 5. Review and approval
Define required reviewers by risk and artifact type. Safety cases, regulated compliance, security exceptions, legal documents and production release baselines require qualified human review. AI-generated content is DRAFT until reviewed.
