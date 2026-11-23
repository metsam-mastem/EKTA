# What Is EKTA?
**Document ID:** EKTA-USER-WHAT-0001 | **Status:** DOCUMENTATION BASELINE

## 1. Definition
EKTA (Engineering Knowledge & Techniques Atlas) is an engineering knowledge operating environment. It organizes concepts, techniques, methods, patterns, standards, tools, implementations, evidence and typed relationships so engineering knowledge can be discovered, understood, connected, evaluated, used in decisions, executed and verified.

It is not merely a glossary, file dump, prompt library, project tracker or AI chatbot. Its intended value is a structured, versioned and inspectable body of engineering knowledge with stable identities, provenance and relationships.

## 2. Why it exists
Engineering knowledge is fragmented across specifications, source repositories, papers, standards, issue trackers, CAD files, test reports, personal notes and conversations. This creates repeated research, inconsistent terminology, hidden assumptions, weak traceability and decisions that cannot be reconstructed.

EKTA addresses these problems through canonical identities, independent taxonomy axes, typed graph relations, provenance, versioning, evidence, explicit uncertainty and a path from discovery to decisions and practices.

## 3. Four workspaces
- **DISCOVERY:** investigate problems; find sources, repositories, standards, papers, tools and candidate concepts. Capture search scope, date, source, method and confidence.
- **ENCYCLOPEDIA:** maintain reviewed canonical records: definitions, purpose, architecture, mechanisms, inputs/outputs, lifecycle, interfaces, trade-offs, implementations, failure modes and evidence.
- **DECISION LAB:** compare alternatives, expose assumptions, assess risks and trade-offs, and record rationale, rejected options, consequences and review triggers.
- **EXECUTION LAB:** convert decisions into plans, procedures, tests, experiments, implementation tasks, acceptance criteria and evidence.

The cycle is iterative. Failures and operational observations can reopen discovery or revise a concept.

## 4. Knowledge objects
Objects may include concepts, techniques, methods, patterns, standards, tools, implementations, architectures, projects, requirements, decisions, tests, evidence and releases. Native artifacts such as PDF, CAD, source trees, datasets and recordings retain their original formats; EKTA should store identity, metadata, provenance and relations rather than flattening every artifact into text.

## 5. Classification axes
- Engineering Territory: broad navigation/portfolio territory.
- Engineering Domain: specialist discipline or operational domain.
- Engineering Layer: where a mechanism/component sits in a system.
- Knowledge Type: concept, architecture, mechanism, algorithm, pattern, method, standard, tool, implementation, evidence, etc.

A record can relate to multiple domains/layers but retains one canonical identity. Reuse existing taxonomy registries; do not create near-duplicate labels.

## 6. UPDS boundary
Universal Project Documentation System (UPDS) is a bounded reusable subsystem proposed for integration across EKTA. EKTA remains the engineering knowledge atlas; UPDS manages project-specific artifacts such as charter, requirements, architecture decisions, plans, risks, changes, tests, evidence, releases and project memory. UPDS should reuse EKTA taxonomy and typed graph contracts rather than duplicate them, while remaining extractable through stable namespaces and interfaces.

## 7. Users and use cases
Learners understand a subject from fundamentals to implementation. Engineers investigate mechanisms and compare designs. Architects record boundaries, interfaces and ADRs. Owners maintain scope, requirements, risks and evidence. Testers/operators execute procedures and capture results. Researchers evaluate sources and create reproducible experiments. AI agents read canonical context, make bounded changes, validate and hand off without chat history.

## 8. Current vs intended capabilities
Repository documentation identifies runtime v0.2 as a local read-only search/explore workbench. Search, facets, concept/document lookup and taxonomy browsing are described in the root README; confirm against the exact branch/commit being used.

Do not assume available: UI editing, authentication, multi-user collaboration, semantic/vector search, automatic source ingestion, AI integrations, offline mobile packaging, full UPDS registry/API, graph traceability engine, dashboard or automatic project starter generation. These require implementation and tests.

## 9. Principles and success measures
Evidence before claims; stable IDs; explicit ownership; Git-native portability; local-first where feasible; human approval for consequential decisions; explicit uncertainty; no silent deletion; native artifact preservation; reproducible validation; chat is an interface, never canonical memory.

Measure time to find trusted answers, provenance coverage, broken-link rate, unresolved-reference rate, requirement-to-test traceability, decision reproducibility, clean-clone recovery, validator pass rate and reuse in a second project. Raw document count is not a quality metric.
