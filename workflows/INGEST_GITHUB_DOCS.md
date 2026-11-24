# GitHub Docs — Source Intake and Maintenance Workflow

**Source:** EKTA-SRC-000009  
**Workflow status:** PROPOSED  
**Owner:** EKTA project owner / delegated reviewer

## Objective
Convert selected GitHub Docs pages into traceable engineering knowledge without confusing source text, EKTA interpretation, canonical concepts, or implementation evidence.

## Pipeline
1. **Discover**
   - Read `https://docs.github.com/llms.txt`.
   - Fetch supported languages and documentation versions from the official pagelist endpoints.
   - Fetch the page list for the selected language/version.
   - Store the discovery snapshot, retrieval time, language, version, and page count.
2. **Select**
   - Select pages by an explicit research question or source topic.
   - Do not assume the entire docs site is equally relevant to EKTA.
   - Route candidates using `references/sources/github-docs-taxonomy-map.yml`.
3. **Retrieve**
   - Fetch article metadata and Markdown body through the official API.
   - Preserve canonical pathname, canonical URL, title, breadcrumbs, product area, document type, and API version where applicable.
   - Record retrieval failures and retry them separately; never silently drop failed paths.
4. **Normalize**
   - Normalize source metadata only; do not rewrite source meaning.
   - Keep source snapshots separate from canonical EKTA concept records.
   - Deduplicate by canonical pathname + language + docs version; track content changes with a content hash.
5. **Analyze in DISCOVERY**
   - Extract candidate concepts, mechanisms, interfaces, methods, standards, tools, and implementation references.
   - Capture exact evidence sections and distinguish normative statements from examples and recommendations.
   - Record ambiguity, version dependence, prerequisites, and limitations.
6. **Model in ENCYCLOPEDIA**
   - Search for existing canonical IDs before proposing a new record.
   - Create or update records using the appropriate EKTA template and taxonomy.
   - Add typed relationships only when supported by evidence.
   - Preserve the source ID and deep link in provenance.
7. **Evaluate in DECISION LAB**
   - Compare alternatives and document trade-offs when the source informs an engineering choice.
   - Do not treat vendor documentation as neutral comparative evidence.
8. **Apply in EXECUTION LAB**
   - Convert validated knowledge into a playbook or implementation checklist only when the task requires it.
   - Define preconditions, expected outputs, failure handling, and verification steps.
9. **Verify and maintain**
   - Re-fetch selected high-change pages on a scheduled review or before consequential use.
   - Compare content hashes and metadata; mark changed records for review.
   - Never auto-promote statuses. A human reviewer approves canonical updates.

## Required source manifest fields
`source_id`, `pathname`, `canonical_url`, `title`, `language`, `docs_version`, `product_area`, `document_type`, `retrieved_at`, `content_hash`, `license_note`, `review_status`, `evidence_sections`.

## Acceptance criteria
- Every imported page has a source ID or a deterministic source key and canonical URL.
- Every page records language and docs version.
- Every failed retrieval is present in a failure ledger.
- No duplicate source key exists for the same pathname/language/version.
- Every taxonomy route resolves to an existing registry value.
- Every proposed concept cites at least one exact source section.
- Source text and EKTA-authored analysis remain distinguishable.
- No bulk article-body mirror is committed until license compatibility and repository policy are explicitly approved.
- A run report records discovered, retrieved, skipped, failed, changed, and reviewed counts.

## Status semantics
- Discovery snapshot: RESEARCHED when captured and inspectable.
- Candidate mapping: PROPOSED until reviewed.
- Concept record: status follows EKTA evidence policy, not source availability.
- Full mirror: NOT_AUTHORIZED by this workflow.
- External media assets: OUT_OF_SCOPE unless separately approved and rights-checked.

## Operational note
The standalone collector kit is a separate utility. Its ZIP is not the same thing as a populated EKTA source corpus. Keep collector code, generated archives, and EKTA's canonical knowledge records as separate artifacts.
