# UPDS Integration Index
**Document ID:** UPDS-INDEX-0001  
**Status:** PROPOSED

This index is the entry point for the integrated documentation architecture.

| Document | Purpose |
|---|---|
| [Integration decision](UPDS_EKTA_INTEGRATION_DECISION.md) | Product boundary and selected architecture |
| [System architecture](UPDS_EKTA_SYSTEM_ARCHITECTURE.md) | Modules, interfaces, source of truth and deployment |
| [Document universe](UPDS_DOCUMENT_UNIVERSE.md) | Full catalog of document families and records |
| [Crosswalk](UPDS_EKTA_CROSSWALK.md) | Mapping to EKTA workspaces, territories and graph |
| [Memory and chat independence](UPDS_PROJECT_MEMORY_AND_CHAT_INDEPENDENCE.md) | Canonical memory, handoff and recovery |
| [Template standard](UPDS_DOCUMENT_TEMPLATE_STANDARD.md) | Metadata, document structure and revision policy |
| [Implementation roadmap](UPDS_IMPLEMENTATION_ROADMAP.md) | Phased delivery and acceptance gates |

## Existing EKTA assets to preserve and integrate
- `docs/CONTEXT_CONTINUITY.md` — canonical resumption order and continuity rules.
- `docs/MASTER_HANDOFF.md` — comprehensive project handoff.
- `docs/END_TO_END_LIFECYCLE.md` — knowledge lifecycle.
- `docs/KNOWLEDGE_ARCHITECTURE.md` — knowledge model.
- `docs/KNOWLEDGE_OPERATING_WORKFLOW.md` — intake and curation workflow.
- `docs/QUALITY_AND_EVIDENCE.md` — quality and evidence principles.
- `decision-lab/ADR/` — existing architectural decisions.
- `schemas/`, `taxonomy/`, `templates/`, `tools/`, `tests/` — canonical technical contracts and validation.

## Current implementation state
The files in this directory define an additive architecture and catalog. They do not claim that document registry runtime, project dashboard, UPDS schemas, automatic memory capture or graph integration have already been implemented. Those remain roadmap work until code and tests demonstrate otherwise.
