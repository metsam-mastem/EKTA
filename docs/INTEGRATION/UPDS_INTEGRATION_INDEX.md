# UPDS Integration Index
**Document ID:** UPDS-INDEX-0001 | **Status:** PROPOSED

This is the canonical entry point for the integrated project-documentation architecture.

## Architecture and contracts
- [Integration decision](UPDS_EKTA_INTEGRATION_DECISION.md) — product boundary and selected architecture.
- [System architecture](UPDS_EKTA_SYSTEM_ARCHITECTURE.md) — modules, interfaces, sources of truth and deployment.
- [Document universe](UPDS_DOCUMENT_UNIVERSE.md) — document families and applicability.
- [Crosswalk](UPDS_EKTA_CROSSWALK.md) — mapping to EKTA workspaces, territories and typed graph.
- [Memory and chat independence](UPDS_PROJECT_MEMORY_AND_CHAT_INDEPENDENCE.md) — canonical memory, handoff and recovery.
- [Template standard](UPDS_DOCUMENT_TEMPLATE_STANDARD.md) — metadata, document structure and revision.
- [Implementation roadmap](UPDS_IMPLEMENTATION_ROADMAP.md) — phases and acceptance gates.

## User documentation
- [User documentation hub](../USER_GUIDE/README.md)
- [What is EKTA?](../USER_GUIDE/WHAT_IS_EKTA.md)
- [User setup](../USER_GUIDE/USER_SETUP.md)
- [User installation](../USER_GUIDE/USER_INSTALLATION.md)
- [User manual](../USER_GUIDE/USER_MANUAL.md)
- [Project administration](../USER_GUIDE/PROJECT_ADMINISTRATION.md)
- [Recovery and continuity](../USER_GUIDE/RECOVERY_AND_CONTINUITY.md)

## Existing EKTA assets to preserve
- docs/CONTEXT_CONTINUITY.md — canonical resumption rules.
- docs/MASTER_HANDOFF.md — comprehensive project handoff.
- docs/END_TO_END_LIFECYCLE.md — knowledge lifecycle.
- docs/KNOWLEDGE_ARCHITECTURE.md — knowledge model.
- docs/KNOWLEDGE_OPERATING_WORKFLOW.md — intake and curation.
- docs/QUALITY_AND_EVIDENCE.md — quality and evidence.
- decision-lab/ADR/ — architectural decisions.
- schemas/, taxonomy/, templates/, tools/, tests/ — technical contracts and validation.

## Current state and boundaries
The branch contains the architecture/catalog, user documentation, a base JSON Schema, validation primitives, repository validator, sample record, unit tests and CI integration. The runtime registry/API, full graph traceability, dashboard, automated project starter and clean-clone recovery drill are not yet implemented/verified. Do not infer these capabilities from their documentation.

EKTA remains the canonical knowledge atlas. UPDS is a cross-cutting, separable project-documentation subsystem. Integration decision remains PROPOSED pending owner review; this branch is not merged into main.
