# EKTA Project Charter

**ID:** EKTA-GOV-CHARTER-001  
**Version:** 0.1.0  
**Status:** APPROVED  
**Canonical repository:** https://github.com/metsam-mastem/EKTA

## Purpose and problem
Engineering knowledge is fragmented across disciplines, standards, repositories, research papers, vendor documentation, terminology, and individual experience. Similar terms are reused with different meanings across layers. Many documents lack provenance, relationships, lifecycle status, and verification methods. This increases discovery, comparison, reuse, onboarding, and decision costs.

## Vision
A person or engineering system can start from a question or concept, navigate definitions and dependencies, inspect implementations and evidence, compare alternatives, and reach a reproducible engineering action without losing context.

## Mission objectives
- Build a multidimensional taxonomy of engineering domains, layers, and knowledge types.
- Create canonical, versioned concept records with stable identifiers.
- Model typed relationships as a navigable knowledge graph.
- Connect concepts to standards, papers, documentation, source code, tools, and examples.
- Separate facts, interpretations, proposals, and implementation evidence.
- Provide repeatable workflows for discovery, design, decision, implementation, and verification.
- Preserve project context and decision history across sessions and contributors.
- Enable future machine-readable exports, search, graph visualization, learning, and AI-assisted retrieval.

## Scope
**Included:** software engineering; computer architecture and operating systems; electronics, semiconductors, IC design, PCB, firmware and embedded systems; mechanical engineering, materials and manufacturing; systems engineering, control, robotics and automation; data, networking, distributed systems, AI infrastructure, security, safety, reliability, testing, operations, UX/HMI, product and project engineering.

**Excluded unless explicitly approved:** unrelated project repositories; unlicensed third-party source-code copying; treating generated summaries as primary evidence; claiming exhaustive coverage without measurable criteria; treating marketing claims as independent validation; building a production runtime before knowledge-model needs justify it.

## Stakeholders
Engineers, researchers, architects, technical leads, students, maintainers, and AI/retrieval systems consuming structured engineering context.

## Success criteria
- Canonical concepts have stable IDs and required metadata.
- Taxonomy nodes have definitions, parentage, and scope notes.
- Relationships use controlled predicates.
- Claims trace to sources or explicit uncertainty labels.
- Research sources record dates, type, access, and relevance.
- Validators detect missing fields and broken local references.
- Workflows define inputs, outputs, gates, and acceptance criteria.
- Changes are versioned and decisions recorded.

## Principles
1. Evidence before confidence.
2. Explicit uncertainty instead of invented certainty.
3. Stable identifiers and versioned definitions.
4. Separate taxonomy, ontology, and implementation.
5. Cross-layer links without collapsing distinct meanings.
6. Prefer open standards and interoperable formats.
7. Prefer open-source tools when they fit.
8. Reuse upstream code only after license, security, maintenance, and fit review.
9. Design for low-resource and offline-friendly use where practical.
10. Human review for consequential decisions.
11. Small, testable increments over speculative mega-builds.
12. No completion claim without inspectable evidence.

## Deliverables
Charter and governance; master taxonomy; concept, technique, architecture, standard, tool, research and decision schemas; graph model; domain maps; source registry; playbooks and checklists; validation and graph tooling; future search site and interactive graph subject to separate decisions.

## Constraints
GitHub is canonical source of truth. Repository is public: never commit secrets or private data. License is undecided. Standards may be copyrighted or paywalled: record metadata and summaries, not protected text. External source status must be rechecked at use time.

## Governance
Maintainer approval is required for scope changes, license selection, major taxonomy changes, and project-wide architecture. Use RFCs and ADRs for consequential changes. The charter remains proposed until explicitly approved.


## Approval record

**Decision:** APPROVED  
**Date:** 2026-11-23  
**Authority:** Explicit user confirmation in the project conversation.

The approval applies to the current charter and product vision. It does not automatically approve a repository license, implementation stack, hosting provider, or any feature not specified in the charter. The license remains undecided until a separate decision is recorded.
