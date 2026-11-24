# Universal Engineering Knowledge Organization

Status: PROPOSED. Scope: a cross-domain organization view for EKTA, not a replacement for canonical taxonomy registries. Origin: analysis of a handwritten note dated 2021-05-19 and subsequent conceptual expansion.

## 1. Purpose and canonical boundaries

EKTA's canonical classification remains 26 Engineering Territories for navigation and portfolio coverage, 25 Operational Domains for granular tagging, 10 Engineering Layers, 30 Knowledge Types, and controlled relationship predicates.

The 14 macro-areas below are a crosswalk for organizing material. They are not new territories, exclusive disciplines, or mutually exclusive project phases. Their machine-readable mappings are in ../taxonomy/ENGINEERING_ORGANIZATION_VIEW.json.

## 2. Fourteen macro-areas

| ID | Macro-area | Primary concern |
|---|---|---|
| foundations | Foundations and Engineering Sciences | Mathematical, scientific, computational, and systems foundations |
| strategy-governance | Strategy and Governance | Direction, authority, policy, accountability, and portfolio choices |
| requirements | Requirements Engineering | Stakeholder needs, requirements, constraints, acceptance, traceability |
| architecture | Architecture Engineering | Fundamental structures, elements, relationships, viewpoints, decisions |
| design | Engineering Design | Detailed realization of structures, behavior, interfaces, physical form |
| construction | Construction and Implementation | Building, coding, fabrication, integration, configuration |
| verification-validation | Verification, Validation and Test | Evidence that specified requirements and intended needs are met |
| deployment-operations | Deployment and Operations | Release, installation, transition, operation, monitoring, service |
| maintenance-evolution | Maintenance and Evolution | Correction, adaptation, improvement, migration, retirement |
| documentation-knowledge | Documentation and Knowledge | Information products, knowledge records, provenance, learning |
| project-product-management | Project and Product Management | Temporary delivery, product direction, planning, coordination, control |
| quality-security-risk | Quality, Security and Risk | Quality attributes, assurance, threats, hazards, risks, resilience |
| tools-resources | Tools and Engineering Resources | Languages, libraries, frameworks, SDKs, toolchains, standards, sources |
| economics-delivery | Engineering Economics and Value Delivery | Feasibility, cost, value, sourcing, business models, outcomes |

## 3. Hierarchy and graph are complementary

Use hierarchy for decomposition and navigation:
- L0: engineering knowledge system;
- L1: macro-area or canonical territory;
- L2: domain or subdomain;
- L3: topic, system, process, or artifact family;
- L4: concept, method, component, tool, requirement, or document record.

These levels are a local organizational convention, not a universal standard. A record may be classified on multiple orthogonal axes and linked to many records. Do not force all relationships into parent-child form.

Use typed graph edges for cross-cutting relationships such as IS_A, PART_OF, USES, DEPENDS_ON, IMPLEMENTS, VERIFIED_BY, DEFINED_BY, DERIVED_FROM, and SUPERSEDES. Canonical records must use only predicates in the controlled EKTA registry unless a reviewed taxonomy change is accepted.

## 4. Distinguish three questions

1. Knowledge taxonomy: what kind of thing is this?
2. Lifecycle/process: when and how is it created, applied, reviewed, and maintained?
3. Information architecture: what artifact records it, who uses it, and what authority does it have?

An architecture decision is a knowledge object and a project decision record. It may be created during architecture work, referenced by implementation, and verified during review. It is not itself an architecture diagram.

## 5. Core distinctions

- Strategy sets direction and trade-offs; governance defines decision rights and controls.
- A plan organizes intended work, timing, resources, dependencies, and controls.
- A project is temporary; a product is an evolving value-bearing offering.
- Architecture concerns fundamental system structures and decisions; an architecture description represents that architecture.
- A specification states properties or constraints; a requirement expresses a need or obligation to be satisfied.
- A standard is a published normative or consensus document; it is not automatically law or a project requirement.
- A source is the origin of information; a reference is a source used to support a claim.
- Verification evaluates conformance to specified requirements; validation evaluates fitness for intended use and stakeholder need.
- Deployment transitions a release into a target environment; operations sustain the system in use.
- Maintenance changes a system after delivery; evolution includes broader adaptation and capability growth.

## 6. Governance

1. Do not create a parallel canonical taxonomy.
2. Keep territory, domain, layer, and knowledge type independent.
3. Treat macro-area membership as a derived crosswalk, not a canonical tag.
4. Record ambiguity and confidence instead of silently guessing.
5. Record source provenance, edition, access date, and evidence status.
6. Do not claim standards conformance from an index entry alone.
7. Do not promote concepts to VERIFIED or VALIDATED without review evidence.
8. Keep canonical records in Git; generated maps and indexes must be reproducible.
9. Stable IDs are immutable and never recycled.
10. Material changes to canonical axes or predicates require maintainer review and, where appropriate, an ADR.

## 7. Acceptance and next work

- Crosswalk validates against existing territory IDs.
- Documentation states that macro-areas do not replace canonical taxonomy.
- Terminology is linked to primary sources.
- CI runs deterministic validation and regression tests.
- Expand canonical concept records in small reviewed batches, not bulk unverified imports.
