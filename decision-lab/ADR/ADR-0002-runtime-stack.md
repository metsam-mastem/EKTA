# ADR-0002: Initial EKTA Runtime Stack

- Status: Proposed for v0.1 implementation
- Date: 2026-11-23
- Decision owner: Project maintainer
- Scope: Initial local-first read-only runtime

## Context

The repository currently contains canonical Markdown/YAML records, Python validation tools, and a small unit-test suite. It does not yet contain an application runtime or user-facing knowledge workbench. The project charter requires Git to remain the canonical source of truth and favors open standards, low-resource operation, and incremental delivery.

## Decision drivers

- Preserve the existing repository and knowledge model.
- Minimize operational cost and dependency count.
- Support offline/local execution.
- Provide a stable API contract for future web, desktop, Android, CLI, and AI clients.
- Keep derived indexes reproducible and avoid premature database lock-in.
- Make correctness testable in GitHub Actions.

## Proposed stack

- Python 3.11+
- FastAPI for the read-only HTTP API
- PyYAML safe parsing for existing YAML and Markdown front matter
- Git-native Markdown/YAML as canonical storage
- Static HTML/CSS/JavaScript for the first browser explorer
- unittest for the initial automated test suite

## Consequences

Positive:
- Reuses the existing Python toolchain.
- Runs locally without a managed database.
- Provides OpenAPI documentation.
- Keeps content reviewable and version-controlled.
- Leaves room for later graph, search, desktop, and mobile adapters.

Trade-offs:
- Markdown front matter is less expressive than a fully normalized database schema.
- Basic text search is not semantic search.
- Static UI is intentionally limited in the first increment.
- Relationship resolution depends on consistent canonical labels or stable IDs.

## Boundaries

The v0.1 runtime is read-only. It must not mutate canonical content, promote status labels, or ingest third-party material automatically. Authentication, persistence, semantic search, AI integration, and hosting are excluded until separate ADRs and acceptance criteria exist.

## Acceptance criteria

- Runtime starts locally from the repository root.
- Health, overview, concepts, taxonomy, and graph endpoints return documented structures.
- Concept IDs remain stable.
- Invalid relationship predicates and unresolved targets are exposed as quality findings.
- Tests run in CI on Python 3.11+.
- No database or paid external service is required.
