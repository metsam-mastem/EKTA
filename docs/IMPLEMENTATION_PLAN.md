# EKTA Implementation Plan

**Product target:** EKTA Engineering Knowledge Workbench  
**Planning baseline:** 2026-11-23  
**Current implementation branch:** main (user documentation PR #4 merged)  
**Delivery principle:** ship verified vertical slices; never label a phase complete because its plan or documentation exists.

## Product definition of done — v1.0

EKTA v1.0 is a usable, local-first engineering knowledge workbench when a user can:

1. Discover engineering concepts and sources through structured search and filters.
2. Inspect canonical records with stable IDs, taxonomy, evidence, provenance, and revision history.
3. Navigate a typed graph across concepts, tools, standards, implementations, and workflows.
4. Compare alternatives in Decision Lab with explicit criteria, assumptions, trade-offs, and evidence.
5. Use Execution Lab playbooks with inputs, prerequisites, steps, acceptance criteria, and verification evidence.
6. Export and import portable knowledge bundles without losing IDs, links, or provenance.
7. Run the core experience locally without a paid hosted database or mandatory AI provider.
8. Rebuild all derived indexes deterministically from the canonical Git repository.
9. Validate content, schemas, graph edges, tests, and release artifacts in CI.
10. Understand what is verified, proposed, incomplete, stale, or blocked.

## Delivery stages

### Stage 0 — Runtime foundation and independent onboarding (v0.1–v0.3)
Status: VALIDATED and merged to main at commit 0d53a9131dad1aeca4c909493871b2ad7b41a225. Its final feature-branch CI passed 17 tests, schema/documentation validation, and graph export.

Deliverables:
- Python 3.11+ package and local launch scripts.
- FastAPI read-only API.
- Safe Markdown/YAML loader.
- Concept list, detail, taxonomy, and graph services.
- Minimal browser explorer.
- CLI overview and graph export.
- Unit and API smoke tests.
- CI validation and graph export.

Additional documentation deliverables (v0.3):
- Independent Persian-first user documentation index, project overview, setup, installation, manual, and input guide.
- Chat-independence and recovery protocol, troubleshooting, and agent/developer onboarding.
- README navigation and repository continuity updated to point to canonical user documentation.

Exit gate:
- All automated tests pass on the exact release candidate commit.
- Runtime API and browser root are exercised by tests.
- Local setup instructions work on Windows and Linux/macOS.
- A new user can follow the documentation without relying on chat history; usability onboarding still requires a separate user test.

### Operational Workspace slice — v0.4
Status: VALIDATED and merged to main. Final PR-head CI run #146 completed SUCCESS.

Deliverables in this slice:
- First-run onboarding flow and self-test API/UI.
- Markdown/YAML/JSON import staging with size limits and safe parsing.
- Draft editor storing proposed concept records outside canonical encyclopedia.
- ZIP backup export over an explicit allowlist and restore preview staging with traversal/symlink checks.
- Markdown documentation center with scoped reads under docs/.

Safety boundary: no direct canonical writes, Git operations, archive extraction, authentication, or network exposure hardening. See `docs/WORKSPACE_GUIDE.md` and `docs/SECURITY_AND_STAGING_MODEL.md`.

### Stage 1 — Knowledge integrity (v0.2)
Status: IN PROGRESS. The canonical 26-territory navigation registry and 25 operational domain tags are published and CI-validated, with explicit territory-to-domain mappings. The concept JSON Schema, duplicate-ID check, taxonomy and territory mapping validation, and local link validation are active. Remaining work includes broader record schemas, a canonical ID registry, canonical relationship target IDs, and graph integrity enforcement.

Deliverables:
- Machine-readable JSON Schema for concepts, sources, techniques, decisions, and workflows.
- Canonical registries for domains, layers, knowledge types, relations, and IDs.
- Duplicate-ID, missing-field, invalid-taxonomy, invalid-predicate, and dangling-edge checks.
- Relationship records standardized around stable IDs.
- Graph export with generator version and source revision.
- Data-quality report separating errors, warnings, and unresolved references.

Exit gate:
- All canonical records validate against schemas.
- Every relationship has a controlled predicate and a resolvable target, or an explicit unresolved/proposed status with rationale.
- CI blocks invalid records and graph regressions.

### Stage 2 — Discovery and retrieval (v0.3)
Status: IN PROGRESS. A deterministic lexical search baseline indexes concepts and selected repository Markdown/YAML/JSON documents; supports free text, exact phrases, hashtags, field selectors, ranking, snippets, pagination, and facets. Persian/Arabic character normalization is included. CI covers the query and API behavior. Relevance benchmarking, richer bilingual synonyms, and source freshness tracking remain outstanding.

Deliverables:
- Exact, prefix, alias, and full-text search.
- Faceted filters for domain, layer, type, status, evidence, and source.
- Persian/English terminology and synonym model.
- Source registry with publication/update dates, source class, access, license, and trust assessment.
- Search result provenance and stale-source indicators.

Exit gate:
- Search relevance test corpus and measurable acceptance thresholds.
- Every result links to its canonical record and source evidence.

### Stage 3 — Interactive Encyclopedia and graph (v0.4)
Status: IN PROGRESS. The first Persian RTL responsive explorer is implemented with search, 26-territory and domain filters, layer/type/status filters, tag chips, result cards, concept/document detail views, metadata, and graph relationship panels. CI verifies HTML structure, required controls, and JavaScript syntax. A full interactive graph canvas, end-to-end browser interaction tests, keyboard-focused navigation review, and visual browser QA remain outstanding.

Deliverables:
- Full concept reader with cross-links and revision history.
- Interactive graph explorer with neighborhood traversal and filters.
- Cross-layer maps and domain maps.
- Related concepts, implementations, standards, techniques, and source panels.
- Keyboard and mobile navigation.

Exit gate:
- Critical navigation flows work on desktop and Android-sized screens.
- Graph interactions remain usable with a growing corpus.

### Stage 4 — Decision Lab (v0.5)
Status: NOT STARTED.

Deliverables:
- Structured alternatives and decision criteria.
- Weighted comparison matrices with explicit assumptions.
- Evidence-linked trade-offs, risks, cost, and constraints.
- ADR generation and decision history.
- Human approval gates for consequential decisions.

Exit gate:
- A decision can be reproduced from its criteria, inputs, evidence, and revision.

### Stage 5 — Execution Lab and Practice Library (v0.6)
Status: NOT STARTED.

Deliverables:
- Playbooks, techniques, procedures, checklists, and test plans.
- Inputs, prerequisites, outputs, responsible roles, and stop conditions.
- Acceptance criteria and verification evidence.
- Links from practices to concepts, standards, tools, and implementation examples.

Exit gate:
- Each published playbook has a bounded scope, prerequisites, safety notes where relevant, and measurable completion criteria.

### Stage 6 — Local-first distribution and integrations (v0.8)
Status: NOT STARTED.

Deliverables:
- Installable offline-capable web application.
- Export/import bundles and local cache.
- Optional desktop packaging.
- Android delivery path selected after device and browser verification.
- Provider-neutral AI adapter contract; no mandatory external model.
- Optional integrations remain disabled until explicitly configured.

Exit gate:
- Core browse/search/inspect flows work offline after initial content sync.
- No critical workflow depends on a single cloud vendor.

### Stage 7 — Release hardening (v1.0)
Status: NOT STARTED.

Deliverables:
- Security and dependency review.
- Accessibility and responsive UI review.
- Performance budgets and large-corpus tests.
- Backup, restore, and migration tests for any added persistence.
- License decision and third-party attribution audit.
- Release notes, versioned bundle, and reproducible build evidence.

Exit gate:
- All v1.0 definition-of-done items are demonstrated with evidence.
- No unresolved critical/high defects.
- License and content reuse policy are explicit.
- Release candidate CI and acceptance tests pass.

## Non-goals until justified

Do not add a graph database, cloud database, authentication, multi-user editing, autonomous ingestion, semantic embeddings, or mandatory hosted AI merely because they are technically available. Each requires a measured need, cost/security analysis, and a separate architecture decision.

## Current known gaps

- The taxonomy model now distinguishes 26 approved top-level engineering territories from 25 operational domain tags. Some territory mappings or content areas remain intentionally empty until supported by canonical records.
- Current graph extraction finds 29 relationship statements in seven concept records, but only two currently resolve to known concepts. The unresolved and invalid-predicate edges are intentionally exposed.
- Canonical knowledge remains read-only through the runtime. Workspace 0.4 adds local import staging and draft files outside canonical paths; promotion and direct canonical editing are not implemented. Decision Lab, Execution Lab, and all four complete workspaces remain incomplete.
- License selection remains undecided and is a v1.0 release gate.
- A live hosted preview has not been provisioned; the current evidence is GitHub Actions CI and automated API tests.


## Parallel subsystem program — 2026-11-24

Status: ORCHESTRATED; subsystem PRs remain independently proposed/review-pending.

The active work queue is maintained in `orchestration/WORKSTREAMS.yml` and documented in `docs/ORCHESTRATION/ACTIVE_WORKSTREAMS.md`. Nine open PRs are tracked: USDO #13, UMSF #11, MUA #19, VEL #10, VES #20, Collaboration Atlas #9, GitHub Docs #8, archive intake #7, and UPDS #3. No subsystem is approved by inclusion in the registry. Exact-head CI, schema/semantic review, and owner approval remain required.
