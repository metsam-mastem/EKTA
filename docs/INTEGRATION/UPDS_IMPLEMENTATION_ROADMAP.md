# UPDS–EKTA Implementation Roadmap
**Document ID:** UPDS-PLAN-0001  
**Status:** PROPOSED

## Phase 0 — Preserve and establish baseline
- Capture current EKTA branch, commit, tree and CI baseline.
- Additive integration ADR and architecture.
- No deletion, rename or schema migration.
**Exit:** baseline and no-loss policy recorded.

## Phase 1 — Catalog and crosswalk
- Publish document universe and applicability rules.
- Map catalog to EKTA's 26 territories, four workspaces and existing records.
- Identify duplicates and canonical ownership.
**Exit:** all document families have an owner and mapping.

## Phase 2 — Shared metadata and identifiers
- Define UPDS artifact schema and ID namespace.
- Define status dimensions, evidence object and typed relations.
- Add templates for charter, requirements, ADR, risk, test, change, release and handoff.
**Exit:** schema validates sample records; no collision with EKTA IDs.

## Phase 3 — Memory and continuity
- Add current state, decision register, active work, open issues, evidence index, recovery guide and session handoff.
- Reconcile with existing context continuity and master handoff.
**Exit:** clean clone can resume a task without chat.

## Phase 4 — Validation and policy gates
- Validate metadata, IDs, statuses, references, required sections, broken links and traceability.
- Add CI checks without breaking existing checks.
- Add secret scanning and evidence checks where feasible.
**Exit:** local and CI validation are reproducible.

## Phase 5 — Integrated knowledge graph
- Extend graph model to represent documents, requirements, decisions, components, tests, evidence and releases.
- Preserve existing concept graph nodes/edges.
- Add crosswalk and graph consistency checks.
**Exit:** query path from objective to release evidence and back to reusable concept.

## Phase 6 — Workbench integration
- Search and filter document registry.
- Display document/concept cross-links.
- Show project state, baseline, decisions, gaps and handoff.
- Keep offline-first behavior.
**Exit:** working user flow verified in runtime and tests.

## Phase 7 — Automation and project starter
- Generate document sets from project type and risk profile.
- Applicability/tailoring engine; document completeness dashboard.
- Exportable project starter and portable archive.
**Exit:** generated project can be cloned, validated and resumed independently.

## Phase 8 — Product extraction readiness
- Package UPDS schemas, templates, catalog and validators behind stable interfaces.
- Test use in a second sample project.
- Decide whether to publish standalone UPDS repository/package.
**Exit:** independent reuse demonstrated without EKTA dependency leakage.

## Priority rules
1. Preserve current EKTA behavior and knowledge.
2. Complete canonical contracts before UI expansion.
3. Build validators before bulk population.
4. No heavy database or hosted dependency until justified.
5. All phases require evidence; NOT_RUN and BLOCKED remain explicit.
