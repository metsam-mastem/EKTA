# GitHub Docs Integration into EKTA

## Decision
Register GitHub Docs as a curated, version-aware primary technical documentation source. Do not create a new engineering territory for it and do not bulk-copy the entire documentation corpus into the EKTA canonical repository.

## Why this integration model
EKTA's architecture separates territories, operational domains, engineering layers, knowledge types, source provenance, and canonical concept identity. GitHub Docs spans multiple engineering areas: source control, collaboration, CI/CD, APIs, security, administration, development environments, and AI-assisted development. It therefore belongs in the source/research layer and routes into existing taxonomy dimensions.

## Components added by this integration
- Source record: `research/sources/EKTA-SRC-000009-github-docs.md`
- Research register entry: `EKTA-SRC-000009`
- Topic crosswalk: `references/sources/github-docs-taxonomy-map.yml`
- Intake and maintenance procedure: `workflows/INGEST_GITHUB_DOCS.md`
- Standalone collector kit: external companion artifact; not part of this repository commit.

## Source/API contract
The official GitHub Docs API exposes page discovery, version/language discovery, search, article metadata, and Markdown body retrieval. Start from `https://docs.github.com/llms.txt`, then use the official API reference:
`https://docs.github.com/en/get-started/using-github-docs/github-docs-api`.

The English `free-pro-team@latest` page list was previously observed to contain 3,223 lines/paths. Treat this only as a dated snapshot; rerun discovery for current counts and do not equate path count with unique article count.

## EKTA lifecycle routing
- **DISCOVERY:** find pages, capture source metadata, assess evidence and identify candidate knowledge.
- **ENCYCLOPEDIA:** create canonical concept/technique/architecture records only after duplicate and taxonomy checks.
- **DECISION LAB:** compare options and record source-backed trade-offs.
- **EXECUTION LAB:** derive reviewed implementation procedures, checklists, and verification steps.

## Data and licensing boundary
GitHub states that documentation content in the public `github/docs` repository's `assets`, `content`, and `data` directories is CC BY 4.0, while repository code is MIT. This must not be generalized to all embedded third-party assets or linked materials. EKTA's own repository license remains undecided. This integration therefore commits only EKTA-authored metadata, mappings, links, and procedures; it does not commit a bulk copy of GitHub Docs content.

## Status
- Repository inspected: PASS.
- Official API model documented: PASS.
- Source identity registered: proposed in this branch.
- Taxonomy crosswalk: PROPOSED; automated validation pending.
- Bulk page download: NOT_RUN in this environment.
- Complete offline corpus: NOT_BUILT.
- Canonical concept extraction: NOT_RUN.
- Merge to `main`: NOT_REQUESTED; review via pull request first.

## Next steps after review
1. Review and merge this integration PR.
2. Run the collector outside the restricted execution environment, initially with a small `--limit` test.
3. Save the generated archive outside EKTA's canonical knowledge directories.
4. Produce a source manifest and failure ledger.
5. Select high-value GitHub Docs categories for staged knowledge extraction.
6. Add deterministic taxonomy/manifest validation to CI before scaling ingestion.
