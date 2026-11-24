# Changelog

## 0.2.0 — Search and Explore Workbench

- Added unified deterministic search across concept identities and selected repository Markdown/YAML/JSON records.
- Added free-text AND matching, exact phrases, hashtags, field selectors, ranking, snippets, result pagination, and search facets.
- Added scoped document IDs and a document-detail API; arbitrary filesystem-path reads are not exposed.
- Added Persian/Arabic character normalization and a Persian-first RTL browser explorer.
- Added identity-card detail tabs for content, relationships, and metadata; added territory/domain/layer/type/status/source filters.
- Formalized the 26 top-level engineering territories separately from 25 operational domain tags.
- Added a repeatable knowledge intake workflow, work-item template, and pull-request review checklist.
- Extended CI validation to enforce 26 unique territories and valid territory-to-domain mappings.
- Added search parser, territory filter, API, document detail, and RTL shell tests.

## 0.1.0 — Runtime foundation

- Added Python local-first runtime package and FastAPI read-only endpoints.
- Added canonical concept loading, taxonomy access, and typed relationship extraction.
- Added the initial browser concept explorer and CLI graph export.
- Added JSON Schema for canonical concept front matter and schema/taxonomy validation.
- Added automated API, runtime, schema, and repository tests.
- Added runtime architecture and implementation planning documents.

## Repository bootstrap — 2026-11-23

- Established the EKTA charter, governance, taxonomy, knowledge architecture, lifecycle, source registers, templates, and master handoff.
- Approved the charter and product vision on 2026-11-23.
- License remains undecided; no downstream reuse permission should be inferred from repository visibility.

## 0.3.0 — Independent user and continuity documentation

- Added a central Persian-first user documentation index.
- Added project overview covering what EKTA is, why it exists, product spaces, lifecycle, taxonomy, architecture, use cases, current features, and explicit non-features.
- Added user setup and platform installation instructions for Windows, Linux, and macOS based on the actual launch scripts and dependencies.
- Added a comprehensive workbench manual for search, hashtags, exact phrases, field selectors, filters, result cards, identity records, documents, and read-only API.
- Added an input guide separating search query input from canonical knowledge contribution and documenting supported file types and ingestion limitations.
- Added independence and recovery protocol so project context is preserved in Git rather than chat history.
- Added troubleshooting and AI/developer onboarding procedures.
- Updated README navigation, repository map, and context continuity handoff.
- Documented that deleting a ChatGPT conversation does not delete GitHub repository content, while uncommitted chat-only decisions may be lost.
- Explicitly documented current non-features: no UI upload/edit, semantic/AI search, authentication, multi-user cloud, Android package, or production public deployment.

## Operational Workspace v0.4 — 2026-11-23

- Added first-run onboarding and repository self-test.
- Added bounded Markdown/YAML/JSON import staging; canonical knowledge remains unchanged.
- Added a Git-separated draft editor for proposed concept records.
- Added allowlisted ZIP backup export and safe restore preview staging; no automatic overwrite.
- Added a Markdown documentation center.
- Added API tests and user/security documentation for the new workflows.

### Workspace verification hardening

- Enforced the canonical `EKTA-CON-######` draft ID format and blocked collisions with existing canonical concept IDs.
- Added metadata bounds, malformed YAML rejection, restore traversal regression coverage, and workspace UI JavaScript/structure validation.
- Replaced HTML string interpolation in documentation listing and backup-link rendering with DOM text nodes.


## VEL 0.1.0 — Visual engineering language foundation (2026-11-24)

- Added VEL specification, card/connector catalog, open-source research register, and phased roadmap.
- Added canonical JSON Schema and a local Python semantic validator for node/port/connection/group integrity.
- Added deterministic DOT export and a local-AI-workstation example model.
- Added unit tests and EKTA integration boundaries; no external source code was vendored.
- Visual editor, QR/camera ingestion, and third-party adapters remain planned, not implemented.
