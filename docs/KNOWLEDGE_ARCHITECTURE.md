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
