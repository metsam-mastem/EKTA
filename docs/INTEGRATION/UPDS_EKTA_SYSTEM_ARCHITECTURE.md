# UPDS–EKTA Integrated System Architecture
**Document ID:** EKTA-ARC-0001  
**Status:** PROPOSED  
**Version:** 0.1.0

## 1. Product model
EKTA is the engineering knowledge atlas and knowledge operating environment. UPDS is its reusable project documentation, governance, memory and lifecycle subsystem. The integrated system is a **knowledge-to-engineering continuity platform**.

```mermaid
flowchart TB
  UI[Web / Desktop / Android / CLI / API / AI adapters]
  UX[DISCOVERY | ENCYCLOPEDIA | DECISION LAB | EXECUTION LAB]
  APP[Application and workflow services]
  SHARED[Shared contracts: IDs, metadata, status, relations, evidence, provenance]
  EKTA[EKTA Knowledge Core: taxonomy, concepts, techniques, standards, tools, graph]
  UPDS[UPDS Project Core: documents, templates, records, memory, lifecycle, governance]
  STORE[Git-native canonical source + portable exports]
  CI[Validation, tests, policy gates, graph/index builds]
  UI --> UX --> APP --> SHARED
  APP --> EKTA
  APP --> UPDS
  EKTA <--> UPDS
  EKTA --> STORE
  UPDS --> STORE
  STORE --> CI
  CI --> APP
```

## 2. Architectural principles
1. **Knowledge is not a project record.** A canonical concept describes generally applicable engineering knowledge; a project document records a particular project's intent, design, state or evidence.
2. **One fact, one canonical owner.** Avoid duplicate authoritative copies. Other views link to the owning record.
3. **Git-native first.** Markdown/YAML/JSON and source code remain inspectable, diffable, cloneable and usable offline.
4. **Portable and replaceable tools.** No mandatory hosted database, proprietary agent, single AI provider or chat session.
5. **Explicit epistemic status.** Proposed, researched, verified, implemented and validated are not interchangeable.
6. **Traceability by stable IDs.** Links should survive file moves and interface changes.
7. **Human approval for controlled baselines.** AI may draft, classify and detect gaps; it must not silently approve requirements, architecture, safety, release or legal decisions.
8. **Evidence before claims.** A build, test, release or migration is complete only when its evidence is recorded.
9. **Progressive complexity.** Start with files and validators; add databases, graph stores and workflow engines only when demonstrated needs justify them.
10. **No destructive integration.** Preserve source content, identifiers, historical decisions and superseded baselines.

## 3. Bounded modules
### EKTA Knowledge Core
- Engineering territories/domains/layers/knowledge types.
- Concepts, techniques, methods, patterns, standards, tools, implementations.
- Research sources, evidence and provenance.
- Typed knowledge graph and cross-layer maps.
- Discovery, encyclopedia, decision and execution workspaces.

### UPDS Project Core
- Document taxonomy and document register.
- Project charter, business/product, requirements, architecture and design artifacts.
- Software, hardware, firmware, manufacturing and integration records.
- Execution, work packages, schedule, quality, tests and evidence.
- Risk, issue, change, configuration, security, safety and compliance.
- Memory, session handoff, state snapshots and recovery.
- Release, operations, maintenance, improvement and retirement.

### Shared services
- Identity and namespace registry.
- Metadata and lifecycle state model.
- Relationship and traceability service.
- Evidence/provenance service.
- Search/index/export.
- Validation and policy gates.
- Audit/change history.

## 4. Information classes and source of truth
| Information class | Canonical owner | Examples |
|---|---|---|
| General engineering knowledge | EKTA | Runtime concept, FMEA method, PCB design technique |
| Project-specific intent | UPDS | Project charter, scope, requirements |
| Project-specific design | UPDS, linked to EKTA concepts | System architecture, API design, schematic |
| General standard/reference | EKTA reference library | Standard identity, edition, source |
| Project compliance assessment | UPDS | Applicability, gap assessment, evidence |
| Decision | UPDS decision record | ADR, trade-off, approval |
| Execution state | UPDS | Task, build, test, release, incident |
| Reusable lesson | EKTA after review | Generalized technique or failure pattern |
| Raw session/chat | External source or archive | Conversation export; never canonical by itself |

## 5. Cross-workspace integration
- DISCOVERY captures sources, candidate concepts, project research briefs and evidence.
- ENCYCLOPEDIA stores reviewed general knowledge and links project documents to canonical concepts.
- DECISION LAB consumes EKTA knowledge and creates UPDS decision records with alternatives, criteria, rationale and approval.
- EXECUTION LAB uses UPDS work packages, procedures, test plans and evidence, then proposes reusable knowledge back to EKTA.

## 6. Project/document lifecycle
`CAPTURED → DRAFT → IN_REVIEW → APPROVED → BASELINED → IMPLEMENTED (where applicable) → VERIFIED → VALIDATED → SUPERSEDED / ARCHIVED`
Not every document uses every state. A policy, design specification, test report and operational log require different state transitions. State transitions must be type-aware and retain history.

## 7. Deployment modes
- **Repository-only:** Git + Markdown/YAML/JSON + Python validators; full offline authoring and reading.
- **Static portal:** generated documentation and search index; no server required for core knowledge.
- **Local workbench:** local API, local index/graph and local file system.
- **Optional hosted collaboration:** replaceable sync, issue tracker or review service; never the only source of truth.
- **AI-assisted mode:** local or remote model adapters with citation/provenance, context package and human approval.

## 8. Security and resilience
- No secrets in repository; use environment variables and secret managers.
- Classify public/internal/confidential/restricted project material.
- Minimize personal data; define retention and deletion rules.
- Sign or hash release artifacts where useful.
- Back up Git remotes and portable archives; test restore.
- Treat model outputs and external source text as untrusted until reviewed.
- Ensure offline access to current baseline, requirements, decisions, schemas and handoff.

## 9. Non-goals for initial integration
No immediate rewrite of EKTA runtime, no forced database migration, no replacement of existing taxonomy, no mandatory external SaaS, no automated approval of engineering baselines, and no claim that all cataloged document types must exist in every project.
