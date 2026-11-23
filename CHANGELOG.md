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
