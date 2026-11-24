# EKTA Knowledge Architecture

## Intent
EKTA uses a layered knowledge architecture with independent classification dimensions and a typed graph. Canonical Markdown/YAML in Git is authoritative; indexes and visualizations are derived and reproducible.

## Three orthogonal axes
**Domain:** software, computer, electrical/electronic, mechanical, systems, control, robotics, manufacturing, networking, security, data, AI, human factors.  
**Layer:** mission/requirements; human/experience; application/agent; workflow/orchestration; service/data; platform/runtime; operating system; firmware/control; hardware architecture; physical implementation.  
**Knowledge type:** concept, principle, architecture, component, interface, technique, method, pattern, process, standard, tool, metric, failure mode, research, decision, playbook, test, implementation.

A concept can have multiple domain and layer tags. Do not force exclusive classification.

## Node types
Concept, Domain, Layer, KnowledgeType, Technique, Architecture, Component, Interface, Standard, Tool, Source, Decision, Workflow, Test, Metric, FailureMode, Implementation.

## Relationship vocabulary
IS_A, PART_OF, USES, DEPENDS_ON, IMPLEMENTS, EXTENDS, CONTROLS, EXECUTES, SCHEDULES, OBSERVES, CONNECTS_TO, CONSUMES, PRODUCES, VERIFIED_BY, DEFINED_BY, ALTERNATIVE_TO, COMPETES_WITH, RELATED_TO, SUPERSEDES, DERIVED_FROM.

Each edge has subject, predicate, object, optional context, provenance, and status.

## Lifecycle
Discover → Capture → Normalize → Classify → Model → Source → Review → Publish → Apply → Verify → Maintain → Deprecate.

## Source of truth
Canonical records in Git are authoritative. JSON, JSON-LD, graph files, site pages, indexes, and embeddings are derived. Derived artifacts identify generator version and source revision.

## Future search
Exact term and alias; fuzzy search; stable ID; domain/layer/type filters; graph traversal; source and implementation lookup; language-aware synonym search; status/version filters.

## Future graph
Start with Markdown and YAML. Potential exports: JSON, JSON-LD, RDF/Turtle, CSV edges, GraphML. Potential local libraries: NetworkX and RDFLib. Adopt a database only when query and scale needs justify it.

## Quality constraints
No duplicate IDs, dangling references, unknown taxonomy tags, unknown predicates, unsupported status promotion, source without provenance, or graph output without source revision.

## Portfolio navigation layer — 26 engineering territories

The product has 26 approved top-level engineering territories in `taxonomy/territories.yml`. These territories organize navigation and portfolio coverage; they are not a replacement for operational domain tags. The 25 entries in `taxonomy/domains.yml` are more granular classification values. Each territory declares its current `domain_ids` mapping, and a domain may map to more than one territory.

The remaining three classification axes are independent: engineering layer and knowledge type, alongside operational domain. Concepts may belong to several values on each axis. Territory membership is derived from the explicit registry mapping; empty mappings indicate a knowledge coverage gap, not an invented association.

## UMSF — semantic coordinate and relationship framework

EKTA's Universal Multidimensional System Framework (UMSF) is being developed as a governed subsystem under `architecture/umsf/`. It extends the existing taxonomy and graph model; it does not replace them.

UMSF defines a view-relative semantic address `(X, Y, Z, T)`:
- X: architectural layer ID from `taxonomy/layers.yml`;
- Y: stable functional module/subsystem identity, not an engineering-domain tag;
- Z: non-negative decomposition depth relative to a declared root and view;
- T: temporal validity, with record time/revision tracked separately.

Typed relationships remain graph edges, not another coordinate. Scope, breadth, scale, viewpoint, view, and context remain explicit qualifiers/metadata. Semantic addresses are not Cartesian measurements; coordinate proximity does not imply dependency, containment, similarity, or execution order.

See [UMSF model specification](../architecture/umsf/MODEL_SPEC.md), [data contract](../architecture/umsf/DATA_CONTRACT.md), [architecture decision ADR-0001](../architecture/umsf/ADR-0001-coordinate-semantics.md), and [research register](../architecture/umsf/RESEARCH_REGISTER.md).

## Runtime discovery contract

The current deterministic search runtime indexes canonical concept records and selected repository Markdown/YAML/JSON content. It supports free-text AND matching, exact phrases, hashtags, stable ID, territory/domain/layer/type/status/kind selectors, result snippets, ranking, pagination, and facets. Search results are discovery projections; canonical files remain authoritative.
