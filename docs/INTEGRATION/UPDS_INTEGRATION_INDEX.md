# UPDS Integration Index
**Document ID:** UPDS-INDEX-0001 | **Status:** PROPOSED

Canonical entry point for the integrated project-documentation architecture.

## Architecture and contracts
- [Integration decision](UPDS_EKTA_INTEGRATION_DECISION.md) — product boundary and selected architecture.
- [System architecture](UPDS_EKTA_SYSTEM_ARCHITECTURE.md) — modules, interfaces and sources of truth.
- [Document universe](UPDS_DOCUMENT_UNIVERSE.md) — document families and applicability.
- [Crosswalk](UPDS_EKTA_CROSSWALK.md) — mapping to EKTA workspaces, territories and typed graph.
- [Memory and chat independence](UPDS_PROJECT_MEMORY_AND_CHAT_INDEPENDENCE.md) — canonical memory, handoff and recovery.
- [Template standard](UPDS_DOCUMENT_TEMPLATE_STANDARD.md) — metadata and revision policy.
- [Input and artifact model](UPDS_INPUT_AND_ARTIFACT_MODEL.md) — intake pipeline, artifact families, provenance and safety.
- [Runtime execution blueprint](UPDS_EXECUTION_BLUEPRINT.md) — service boundaries, proposed API, traceability and delivery stages.
- [Implementation roadmap](UPDS_IMPLEMENTATION_ROADMAP.md) — phases and acceptance gates.

## Supplemental user documentation in this branch
- [User documentation hub](../USER_GUIDE/README.md)
- [What is EKTA?](../USER_GUIDE/WHAT_IS_EKTA.md)
- [Setup](../USER_GUIDE/USER_SETUP.md)
- [Installation](../USER_GUIDE/USER_INSTALLATION.md)
- [Manual](../USER_GUIDE/USER_MANUAL.md)
- [Administration](../USER_GUIDE/PROJECT_ADMINISTRATION.md)
- [Recovery](../USER_GUIDE/RECOVERY_AND_CONTINUITY.md)

The canonical main branch already contains a Persian-first user documentation set at docs/USER_DOCUMENTATION_INDEX.md and linked docs/*.md pages. Consolidate overlapping guides before treating either set as the sole manual.

## Preserve existing EKTA assets
docs/CONTEXT_CONTINUITY.md, docs/MASTER_HANDOFF.md, docs/END_TO_END_LIFECYCLE.md, docs/KNOWLEDGE_ARCHITECTURE.md, docs/KNOWLEDGE_OPERATING_WORKFLOW.md, docs/QUALITY_AND_EVIDENCE.md, decision-lab/ADR/, schemas/, taxonomy/, templates/, tools/ and tests/.

## State boundary
The integration branch contains architecture/catalog, base schema and validator, sample record, unit tests, CI integration and documentation. Runtime registry/API, full graph traceability, dashboard, project starter and clean-clone recovery drill remain NOT IMPLEMENTED or NOT RUN. Integration decision remains PROPOSED pending owner review. No merge to main is implied.
