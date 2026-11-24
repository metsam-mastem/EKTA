---
id: EKTA-SRC-000009
title: "GitHub Docs — Official Product and Platform Documentation"
source_type: official-documentation
status: RESEARCHED
publisher: GitHub
published: continuously-maintained
accessed: 2026-11-24
version: free-pro-team@latest
url: "https://docs.github.com/en"
api_reference: "https://docs.github.com/en/get-started/using-github-docs/github-docs-api"
discovery_index: "https://docs.github.com/llms.txt"
source_repository: "https://github.com/github/docs"
content_license: "CC BY 4.0 (GitHub Docs content; verify individual assets and exceptions)"
code_license: "MIT (public github/docs repository code)"
---
# GitHub Docs — Source Record

## Purpose and relevance
Official technical documentation for GitHub products and platform capabilities. It is a primary documentation source for engineering practices and implementations involving Git hosting, repositories, collaboration, issues, pull requests, Actions, security, APIs, administration, Copilot, and developer workflows.

This source is registered as an external reference. It is not an EKTA engineering territory, not a canonical concept collection, and not an endorsement of every feature or recommendation documented by GitHub.

## Access methods
Use the official documentation API rather than scraping rendered HTML:

- Languages: `GET https://docs.github.com/api/pagelist/languages`
- Versions: `GET https://docs.github.com/api/pagelist/versions`
- Page list: `GET https://docs.github.com/api/pagelist/{lang}/{version}`
- Combined article and metadata: `GET https://docs.github.com/api/article?pathname={encoded_path}`
- Markdown body: `GET https://docs.github.com/api/article/body?pathname={encoded_path}`
- Metadata: `GET https://docs.github.com/api/article/meta?pathname={encoded_path}`
- Search: `GET https://docs.github.com/api/search/v1`
- LLM discovery: `https://docs.github.com/llms.txt`

For external clients, the search endpoint requires a `client_name`; language and version should be explicit for reproducibility. See the API reference for current parameters and examples.

## Initial scope snapshot
A previous live inspection of the English `free-pro-team@latest` page list returned 3,223 lines/paths. This is a dated discovery snapshot, not a guaranteed article count or a current invariant. Recount the page list at each archive run. Paths may include landing pages and other page types.

## Evidence and quality rules
1. Preserve canonical URL, pathname, language, product/version, retrieval timestamp, and source revision or ETag when available.
2. Keep source text separate from EKTA-authored analysis and concept records.
3. Record exact evidence locations (heading/section and URL); do not treat search snippets as sufficient evidence for a technical claim.
4. Distinguish documented product behavior, examples, recommendations, preview/beta functionality, and historical/version-specific behavior.
5. Recheck fast-changing documentation before making current implementation or compatibility claims.
6. Never silently promote a source-derived claim to VERIFIED; use EKTA's evidence/review process.
7. Do not import binary media or third-party assets by default. Track them separately with their own rights and retrieval requirements.

## License and redistribution
The public `github/docs` repository states that documentation content under `assets`, `content`, and `data` is CC BY 4.0 and repository code is MIT. This does not automatically grant identical rights to every embedded image, video, logo, third-party excerpt, or linked resource.

EKTA's repository license is currently undecided. Until EKTA's owner selects a compatible license and an item-level rights review is complete:
- store links, source metadata, page paths, retrieval manifests, and EKTA-authored summaries;
- do not commit a bulk mirror of GitHub Docs article bodies into the canonical EKTA repository;
- retain attribution and license metadata for any permitted excerpts or later imports.

## Related EKTA classifications
See `references/sources/github-docs-taxonomy-map.yml` for proposed crosswalks. The mapping is intentionally many-to-many and is not a claim that all mapped subjects have already been ingested.

## Current status
- Source identity and official API: RESEARCHED.
- Initial taxonomy crosswalk: PROPOSED.
- Full page archive: NOT_RUN in the current environment.
- External media mirror: OUT_OF_SCOPE.
- Canonical concept extraction and verification: NOT_RUN.
