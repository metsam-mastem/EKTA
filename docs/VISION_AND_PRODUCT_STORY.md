# EKTA Vision, Product Story, and Platform Evolution

**Status:** Proposed product direction; not an approved implementation commitment.

## The story

Engineering knowledge currently lives in disconnected places: books, standards, academic papers, Git repositories, vendor manuals, diagrams, issue trackers, and individual memory. EKTA is intended to connect these fragments into a navigable engineering atlas.

The user journey is:

**Question → Discovery → Concept → Relationships → Evidence → Decision → Execution → Verification → Reusable knowledge.**

A person should be able to ask what a runtime is, distinguish platform runtime from workflow runtime, inspect components and implementations, compare Temporal and Airflow without pretending they are equivalent, follow dependencies, and reach a tested design or playbook.

## What EKTA may become

1. **Engineering knowledge repository:** canonical, versioned records and evidence.
2. **Engineering encyclopedia:** structured concepts, terminology, architecture and technique entries.
3. **Knowledge graph:** typed connections among concepts, standards, tools, sources, decisions and implementations.
4. **Research workspace:** source discovery, evidence qualification, and literature synthesis.
5. **Decision lab:** comparison matrices, trade-off analysis, and architecture decisions.
6. **Execution library:** repeatable playbooks, checklists, test plans, and reference implementations.
7. **Interactive atlas:** search, filters, graph exploration, cross-layer navigation, and learning paths.
8. **AI-assisted engineering knowledge interface:** context retrieval and grounded explanations with citations and source provenance.

## Platform evolution proposal

The repository remains the source of truth. A user interface must be a derived client, not a second competing source of truth.

### Stage A — Git-native foundation
- Markdown and YAML records.
- Git history, branches, issues, and pull requests for review and change control.
- Mermaid diagrams stored as text.
- Python standard-library tooling for validation and graph export.
- No mandatory hosted database.

### Stage B — Static web knowledge portal
- Responsive browser interface generated from canonical repository content.
- Full-text search and faceted filters.
- Stable URLs for concept IDs.
- Static hosting and low operational cost.
- Progressive enhancement; core content remains readable without client-side JavaScript.

### Stage C — Local-first atlas
- Downloadable knowledge snapshot.
- Local search index and graph data.
- Offline reading and graph navigation.
- Explicit snapshot version and update mechanism.
- Optional import/export in open formats.

### Stage D — Interactive engineering workbench
- Concept comparison and decision matrices.
- Visual graph exploration and relationship editing proposals.
- Research capture and source evaluation.
- Playbook execution and evidence capture.
- Human approval before publishing canonical changes.

### Stage E — AI-assisted knowledge interface
- Retrieval grounded in canonical EKTA records and cited sources.
- Context packs generated from selected concept neighborhoods.
- Explicit source freshness and confidence metadata.
- No model-generated claim is promoted to VERIFIED without review.
- Human maintainer remains final authority for canonical knowledge.

## Platform targets

| Target | Role | Direction |
|---|---|---|
| GitHub repository | Canonical source of truth | Required |
| Web | Primary discovery and browsing surface | Proposed first UI |
| Desktop | Research, graph exploration, offline work | Future option |
| Android | Portable reading, capture, and offline lookup | Future option |
| CLI/API | Automation and integration | Build as needs emerge |
| AI assistants | Retrieval and explanation interface | Future integration |

## Architecture principles

- Repository-first, not database-first.
- Local-first where feasible; cloud services are optional, not mandatory.
- Open formats and portable exports.
- Stable IDs and canonical URLs.
- Search and graph views derive from canonical records.
- Offline access should not require an online AI model.
- AI features are optional layers; the knowledge base must remain useful without them.
- Avoid premature microservices, mandatory vector databases, and costly infrastructure.

## Product boundaries

EKTA is initially a knowledge system, not a general-purpose workflow runtime, CAD suite, IDE, or replacement for standards bodies. It may document and connect such systems, and later provide integrations, but each expansion requires a use case, architecture decision, and acceptance criteria.

## Open decisions
- Final project charter approval.
- Repository license and separate code/documentation licensing.
- First web documentation stack.
- Whether to adopt MkDocs Material or another static documentation generator.
- Canonical machine-readable record format and formal JSON Schema.
- Graph export format and visualization engine.
- Search engine and offline index strategy.
- Mobile packaging and synchronization approach.
- AI integration and privacy model.

Each decision must be recorded in an ADR before implementation becomes binding.
