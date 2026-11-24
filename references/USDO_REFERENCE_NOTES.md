# USDO Reference Notes and Evidence Register

**Status:** RESEARCHED — initial source review  
**Purpose:** Preserve the public primary references used to shape the first USDO model. This is not a standards-conformance statement.

## Primary references

### 1. ISO/IEC/IEEE 42010:2022 — Architecture description

- Publisher: ISO / IEC / IEEE
- Edition: 2
- Publication date: 2022-11-07
- Official page: https://www.iso.org/standard/74393.html
- Relevance: Specifies requirements for the structure and expression of architecture descriptions, including architecture-description frameworks, architecture-description languages, viewpoints, and model kinds.
- USDO design implication: Distinguish the architecture of an entity from the description that represents it. Allow purpose-specific views rather than assuming one diagram captures every concern.
- Limitation: This standard does not prescribe the process, tools, notation, or a universal ontology for every domain. The USDO facet set is an EKTA design proposal, not a claim of ISO conformance.

### 2. W3C OWL 2 — Structural Specification and Functional-Style Syntax

- Publisher: World Wide Web Consortium
- Recommendation: Second Edition, 2012-12-11
- Official page: https://www.w3.org/TR/owl-syntax/
- Relevance: Defines a formal ontology language with classes, properties, individuals, and data values, together with formal semantics.
- USDO design implication: Keep entity kinds, semantic classes, instances, properties, and typed relations distinct in the conceptual model.
- Limitation: USDO's YAML and JSON Schema records are not OWL ontologies. OWL serialization or reasoning would be a separate interoperability decision.

### 3. OMG UML 2.5.1

- Publisher: Object Management Group
- Formal version: 2.5.1, 2017-12
- Official specification portal: https://www.omg.org/spec/UML/2.5.1
- Official specification overview: https://www.omg.org/spec/UML/
- Relevance: UML provides structural, behavioral, interaction, state-machine, activity, deployment, and other modeling constructs. Its normative machine-readable artifacts include metamodel and diagram-interchange XMI files.
- USDO design implication: Do not collapse static structure, interaction, state, and behavior into a single representation. Use specialized modeling languages as complementary views.
- Limitation: UML is not a universal physical, electrical, or organizational ontology. Domain-specific notations remain necessary.

## Synthesis and design decisions

| Finding | Decision in USDO |
|---|---|
| Architecture descriptions are purpose- and viewpoint-dependent | Architecture and its description are explicitly distinguished |
| Formal ontologies separate classes, properties, individuals, and data values | Ontology, classification, and relations are separate facets |
| Structural and behavioral modeling require different constructs | Architecture/topology are separated from dynamics |
| A single notation does not cover all engineering concerns | USDO is an organizing meta-model, not a replacement for UML, SysML, OWL, schematics, or state models |
| Model scope depends on the purpose of the description | Scope and validity conditions are explicit record fields |

## Evidence and review policy

- The official publisher or standards-body page is preferred over secondary summaries.
- Record edition, publication date, URL, and access context for every adopted reference.
- A reference supports only the claims within its own scope.
- Do not copy normative text into EKTA; record concise interpretations and link to the source.
- Before adopting a standard as normative for EKTA, review the full official text, current edition, licensing/access terms, and applicability.
- Mark conclusions as RESEARCHED until a reviewer verifies the exact claim and its context.

## Not yet researched

The following are explicitly outside this initial source pass:
- Open-source ontology editors, RDF stores, graph databases, and reasoners.
- SysML v2 implementation and interchange ecosystem.
- Circuit netlist interchange and electrical CAD data models.
- Process-modeling and control-system interoperability.
- Formal mapping from USDO JSON Schema records to OWL/RDF or SysML.
- License and maintenance review of candidate open-source libraries.

These items belong to the next research workstream and must not be presented as completed discovery.
