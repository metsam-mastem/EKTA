# UPDS–EKTA Integration Decision
**Document ID:** EKTA-ADR-0003  
**Status:** PROPOSED — pending owner review  
**Date:** 2026-11-23  
**Decision scope:** Product boundaries, repository architecture, knowledge ownership, lifecycle integration.

## 1. Decision
Adopt a **federated integrated architecture**: UPDS (Universal Project Documentation System) becomes an independently specified, reusable documentation-and-lifecycle subsystem embedded in EKTA. EKTA remains the canonical engineering knowledge atlas. UPDS is not reduced to a chapter and is not allowed to absorb or replace EKTA's encyclopedia, taxonomy, discovery, decision, or execution workspaces.

## 2. Why
EKTA already contains a knowledge architecture, typed concepts and relations, evidence/provenance concerns, context continuity, lifecycle documentation, templates, governance, validation tooling, runtime services, and a four-workspace product model. UPDS adds a much broader project-documentation universe: organizational governance, business/product, research, requirements, system/software/hardware architecture, detailed design, manufacturing, execution, verification, security/safety, risk/change/configuration, data, memory, deployment, operations, procurement, legal/compliance, monitoring, release, closure, and retirement.

The overlap is substantial but not identical:
- EKTA answers engineering-knowledge questions and makes knowledge discoverable, comparable, connected, and actionable.
- UPDS defines how project information, controlled documents, records, evidence, changes, handoffs, and lifecycle artifacts are created, governed, linked, retained, and reused.
- Integration connects canonical engineering knowledge to project-specific records without confusing general knowledge with project truth.

## 3. Options considered
| Option | Outcome | Reason |
|---|---|---|
| Keep fully separate | Rejected as default | Duplicates taxonomy, evidence, graph, context and lifecycle mechanisms |
| UPDS as one introductory chapter | Rejected | Documentation and lifecycle controls are cross-cutting, not sequential or introductory only |
| Flatten UPDS into EKTA with no boundary | Rejected | Loses product extraction, independent versioning and reuse |
| Federated subsystem integrated throughout EKTA | Selected | Preserves boundaries while sharing schemas, IDs, graph, validation and UI services |

## 4. Bounded responsibilities
### EKTA owns
- Engineering domain, territory, layer and knowledge-type taxonomies.
- Canonical concept encyclopedia and engineering practice library.
- Research/discovery, knowledge graph, concept provenance and engineering comparisons.
- The four workspaces: DISCOVERY, ENCYCLOPEDIA, DECISION LAB, EXECUTION LAB.

### UPDS owns
- Project document taxonomy and catalog.
- Document lifecycle, templates, document metadata and controlled baselines.
- Project governance, requirements/document traceability, project memory and handoff.
- Project-specific records: decisions, changes, risks, issues, tests, releases, operations and closure evidence.

### Shared platform contracts
- Stable identifiers and typed relationships.
- Evidence and provenance model.
- Status vocabulary with explicit semantic distinctions.
- Versioning, validation, search, graph indexing and export.
- Offline-first, Git-native source of truth.

## 5. Integration placement
UPDS is represented in three ways:
1. **Dedicated domain/territory:** documentation, standards and engineering governance remain a first-class EKTA territory (already present in the 26-territory map).
2. **Cross-cutting capability layer:** document, memory, traceability, configuration and lifecycle services connect every territory and all four workspaces.
3. **Reusable subsystem/package:** UPDS specifications, schemas, templates, catalogs and validators remain under a bounded `upds/` namespace so they can later be extracted without losing history.

Do not force UPDS into the first numbered chapter of the encyclopedia. If a guided learning sequence is needed, introduce it as **Foundation / Part 0: Engineering Governance, Knowledge and Documentation**, before domain chapters, while retaining its cross-cutting links.

## 6. No-loss migration rules
- Do not delete or overwrite existing EKTA material as part of this integration.
- Preserve existing IDs, file paths, taxonomy counts, schemas, runtime behavior and decisions.
- Add integration docs first; modify existing entry points only by additive links and clearly scoped updates.
- If two records overlap, link and reconcile; do not silently merge or discard content.
- Mark proposals as PROPOSED until reviewed; do not backdate approval.
- Keep a migration ledger of every source artifact and its destination.
- Preserve original UPDS catalog content and extend it with EKTA-specific contracts.

## 7. Independence from chat
The repository, not chat history, is canonical. A clean checkout must contain the project identity, current status, architecture, decisions, requirements, open issues, next actions, evidence index, memory protocol, templates, and validation commands. A new agent must resume by reading the repository in the documented order. Chat is an optional transport and collaboration surface only.

## 8. Consequences
Positive: shared knowledge graph, less duplication, cross-domain document coverage, reusable project starter, portable memory and handoff, traceability from engineering concept to implementation evidence.
Costs: more governance, need for clear schemas and namespace boundaries, migration work, and risk of overengineering. Mitigate by implementing the minimum shared contracts first and deferring heavyweight workflow engines.

## 9. Acceptance criteria
- [ ] No existing EKTA file or identifier is removed.
- [ ] UPDS has a bounded namespace and complete catalog.
- [ ] Crosswalk maps UPDS artifacts to EKTA workspaces and existing artifacts.
- [ ] Project memory and context recovery are repository-native.
- [ ] Document metadata, statuses, IDs and relations are specified.
- [ ] Validation checks document inventory, links, IDs, traceability and handoff completeness.
- [ ] Clean-clone resumption procedure is documented.
- [ ] Owner review approves this ADR before treating it as final.

## 10. Reversal
If future use demonstrates unacceptable coupling, extract `upds/` as a separate repository/package using the documented interfaces. No conceptual or record identity needs to change.
