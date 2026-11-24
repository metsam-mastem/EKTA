# UMSF Research Register

**Research snapshot:** 2026-11-24  
**Purpose:** Identify authoritative standards and open specifications relevant to semantic coordinates, architecture descriptions, graph representation, ontology, and provenance. This is a focused first pass, not an exhaustive literature review.

| Source | What it supports | What it does not establish | Access |
|---|---|---|---|
| ISO/IEC/IEEE 42010:2022 | Architecture-description structure; architecture viewpoints and model kinds; applicability to software, systems, enterprises, products and business domains | It does not prescribe a universal coordinate system, a notation, or a storage format | https://www.iso.org/standard/74393.html |
| W3C RDF 1.1 Concepts | Graph data model as subject-predicate-object triples; named graphs and datasets | It does not define EKTA's domain vocabulary or coordinate semantics | https://www.w3.org/TR/rdf-concepts/ |
| W3C OWL 2 Overview | Formal ontology constructs: classes, properties, individuals, data values; RDF-based exchange | It does not require UMSF to adopt OWL or a reasoner | https://www.w3.org/TR/owl-overview/ |
| W3C PROV-O | Interoperable provenance vocabulary; Entity, Activity, Agent and generation/usage relations | It does not automatically provide EKTA's evidence-quality or review policy | https://www.w3.org/TR/prov-o/ |

## Findings applied to UMSF

1. Architecture representation should support multiple views/viewpoints rather than assuming one drawing is the whole architecture. This supports keeping `view_id` explicit.
2. Typed graph edges are a natural separate representation for relationships; they should not be encoded as coordinate axes.
3. Formal ontology export is a possible interoperability path, not a prerequisite for the first local implementation.
4. Provenance should be explicit and linked to entities/assertions/activities; a source URL alone is not a complete evidence assessment.
5. The reviewed standards do not define X=layer, Y=module, Z=depth, T=time. That mapping is an UMSF design decision, not a standards quotation.

## Source quality notes

- ISO and IEEE pages are publisher/standards-body records for the current 2022 edition.
- W3C documents are published technical recommendations/specifications.
- Full ISO/IEEE standard text may be paywalled; this register relies on official public scope/abstract information and does not claim clause-level conformance.
- No external source code has been copied into EKTA in this research pass. The UMSF validator is original, small, dependency-free code.
