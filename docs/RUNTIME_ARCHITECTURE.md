# EKTA Runtime Architecture

**Runtime:** EKTA Knowledge Runtime  
**Initial version:** 0.1.0  
**Implementation status:** Bootstrap implementation in progress  
**Canonical source:** Git-native Markdown and YAML in this repository

## 1. Purpose

The EKTA runtime loads the canonical knowledge corpus and exposes it through deterministic services and interfaces. It is not a second source of truth. Generated graph indexes, API responses, search results, and future visualizations are derived from canonical repository content.

The initial runtime is intentionally read-only. It must never silently rewrite source records or promote their evidence status.

## 2. Runtime boundaries

- **Knowledge source:** encyclopedia/, taxonomy/, references/, research/, and governed records in Git.
- **Content loader:** safe YAML front-matter parsing and canonical record normalization.
- **Knowledge services:** concept lookup, text search, taxonomy access, relationship extraction, and graph projection.
- **API:** versioned HTTP interface under /api/v1.
- **Experience:** lightweight browser explorer served by the runtime.
- **CLI:** inventory and graph export for automation and offline workflows.
- **Validation:** unit tests and GitHub Actions; runtime output is reproducible from a repository revision.

## 3. Technology choice for v0.1

| Concern | Choice | Rationale |
|---|---|---|
| Runtime language | Python 3.11+ | Existing repository tooling and low-friction local execution |
| HTTP API | FastAPI | Typed API contracts and generated OpenAPI |
| Content parsing | PyYAML safe_load | Parse the existing YAML taxonomy and Markdown front matter |
| Source of truth | Git-native Markdown/YAML | Reviewable, versioned, offline-capable, and no database lock-in |
| Initial persistence | None | Avoid premature database operations; canonical content remains in Git |
| Browser interface | Static HTML/CSS/JS | Minimal dependencies and low-resource operation |
| Tests | Python unittest | Compatible with the current repository's standard-library test workflow |

This is a versioned implementation choice, not a permanent platform lock-in. A database, graph database, semantic index, write API, or external AI provider requires a separate evidence-based decision.

## 4. Service contracts

- GET /health — process health and runtime version.
- GET /api/v1/overview — inventory counts and graph resolution summary.
- GET /api/v1/concepts — concept list with q, domain, layer, and status filters.
- GET /api/v1/concepts/{id} — one canonical concept record.
- GET /api/v1/taxonomy — domain, layer, knowledge-type, and relation registries.
- GET /api/v1/graph — graph nodes and typed edges; optional resolved_only and predicate filters.

All endpoints are read-only in v0.1. Unknown concept IDs return HTTP 404. Query results must preserve stable concept IDs and source-file paths.

## 5. Relationship resolution

The graph builder reads the Relationships section from concept records. It validates predicates against taxonomy/relations.yml, then resolves targets by stable ID, canonical name, or alias.

Each edge retains:
- source concept ID;
- predicate;
- resolved target ID, if found;
- original target label;
- resolution status;
- source file.

Unresolved targets and invalid predicates remain visible as quality findings; they are not silently dropped or treated as verified edges. The current concept corpus contains provisional and incomplete relationships, so a non-zero unresolved count is expected during bootstrap.

## 6. Security and integrity

- YAML is loaded with safe_load; no arbitrary object constructors are permitted.
- The initial API exposes repository content only and has no write, shell, or arbitrary file-read endpoint.
- No credentials, secrets, or personal data belong in the public repository.
- Content status is not upgraded by indexing or runtime execution.
- All derived outputs must be reproducible from a known repository revision.
- Third-party standards and source material remain subject to their own rights and license terms.

## 7. Local operation

From the repository root:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
uvicorn ekta_runtime.api:app --app-dir runtime --reload
```

Open http://127.0.0.1:8000. OpenAPI is available at /docs.

CLI:

```bash
ekta overview
ekta graph --output build/knowledge-graph.json
```

Tests:

```bash
python -m unittest discover -s tests -v
```

## 8. Release gates

The runtime is not considered release-ready until:
1. content parsing and taxonomy validation are covered by tests;
2. graph extraction and edge validation are deterministic;
3. API routes and error contracts are tested;
4. the browser explorer is checked at desktop and mobile widths;
5. CI passes on the release candidate commit;
6. documentation and license status are accurate;
7. source revision and generator version are recorded in exported artifacts.

## 9. Explicit non-goals for v0.1

Authentication, multi-user editing, database persistence, semantic embeddings, AI agents, external provider integrations, cloud deployment, and automatic content ingestion are not included in the read-only bootstrap. They require separate threat, cost, governance, and acceptance reviews.
