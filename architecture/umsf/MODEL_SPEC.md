# UMSF Model Specification 0.1

## 1. Problem statement

Complex systems need several simultaneous descriptions: architectural position, functional decomposition, structural depth, relationships, temporal change, and the scope/view through which an observer is examining them. A single hierarchy or graph cannot safely encode all these concerns without conflating different semantics.

UMSF defines a small common model that can be applied to software, hardware, organizations, workflows, knowledge systems, products, and cyber-physical systems.

## 2. Conceptual model

An UMSF model is:

`M = (E, A, G, C, P)`

- `E`: entities with stable identity and type.
- `A`: zero or more semantic addresses assigned to an entity in a declared view.
- `G = (V, R)`: typed relationship graph; vertices reference entities and relations carry predicates.
- `C`: context, scope, viewpoint, constraints, and qualifiers.
- `P`: provenance and temporal assertions.

An address is:

`a = (x, y, z, t)`

where:
- `x` is an architectural layer identifier from EKTA's controlled layer registry;
- `y` is a stable functional module/subsystem identifier, not a domain label;
- `z` is a non-negative decomposition depth relative to a declared root and view;
- `t` is a validity interval or temporal snapshot reference.

The tuple is not a metric vector. X and Y are categorical identifiers; Z is ordinal and view-relative; T is temporal. No arithmetic or geometric distance is defined across these fields.

## 3. Entities and identity

An entity MUST have:
- a stable, non-empty ID;
- a type;
- a canonical name;
- optional description and metadata;
- zero or more addresses.

Identity MUST NOT be derived from coordinates. Moving an entity between layers, modules, views, or time intervals MUST NOT change its ID.

One entity may have multiple addresses because a cross-cutting capability can participate in multiple layers/modules or appear in multiple views. Multiple addresses must not be collapsed into one arbitrary location.

## 4. X — architectural layer

X references an existing EKTA layer ID. The current registry includes mission/requirements, human/experience, application/agent, workflow/orchestration, service/data, platform/runtime, operating system, firmware/control, hardware architecture, and physical implementation.

Rules:
- X MUST reference a known layer ID when validated against the EKTA registry.
- A cross-cutting concern (security, safety, performance, reliability, observability, interoperability, maintainability, accessibility, cost, sustainability) is not automatically a layer.
- An entity may be associated with multiple layers.
- Layer order is a navigation convention, not proof of runtime execution order or a universal stack.

## 5. Y — functional module

Y identifies a functional module, subsystem, service, component group, organizational unit, or other explicitly declared partition of the system under study.

Rules:
- A module has an identity independent of the engineering domain and layer.
- A module may span several layers and domains.
- A domain tag classifies subject matter; it does not identify a module instance.
- Module membership and decomposition are represented explicitly by typed relations such as PART_OF / CONTAINS (if the latter is added to the controlled vocabulary) or by a declared module registry.
- The module coordinate is meaningful only within a declared system/root and view.

## 6. Z — structural depth

Z is a non-negative integer representing decomposition depth from a declared root in a declared view.

Illustrative levels (not mandatory universal names):
- 0: system-of-interest / root;
- 1: subsystem;
- 2: module or component group;
- 3: component;
- 4: subcomponent;
- 5+: implementation element / part.

Rules:
- Depth is relative to the root and view; it is not a global intrinsic property.
- Actual containment must be represented by graph edges or a decomposition tree.
- A graph can be a DAG or contain cross-links; therefore one entity can have different depths in different views or decomposition paths.
- Do not infer containment from a depth difference alone.
- Breadth, scope, scale, and complexity are separate properties/metrics.

## 7. T — temporal dimension

T describes when an assertion or state is valid, and when it was recorded.

Minimum temporal fields:
- `valid_from`: start of real-world/model validity (inclusive);
- `valid_to`: optional end of validity (exclusive);
- `recorded_at`: time the record/change was captured;
- `revision`: repository or model revision.

The distinction between valid time and record time supports correction of historical knowledge without pretending the corrected statement was known earlier. A future extension may adopt a complete bitemporal model and event sourcing, but v0.1 does not implement either.

Rules:
- timestamps SHOULD be ISO 8601 with an explicit UTC offset or Z.
- if both bounds exist, `valid_to` MUST be later than `valid_from`.
- an absent end means open-ended validity, not infinite certainty.
- Git commit history remains the canonical record of repository revisions.

## 8. R — relationships (orthogonal graph)

R is not a fifth coordinate. It is a graph over entities.

An edge contains:
- source entity ID;
- controlled predicate;
- target entity ID;
- optional context;
- evidence/provenance reference;
- assertion status.

Use EKTA's existing relation registry. Typical predicates include IS_A, PART_OF, USES, DEPENDS_ON, IMPLEMENTS, EXTENDS, CONTROLS, EXECUTES, SCHEDULES, OBSERVES, CONNECTS_TO, CONSUMES, PRODUCES, VERIFIED_BY, DEFINED_BY, ALTERNATIVE_TO, COMPETES_WITH, SUPERSEDES, and DERIVED_FROM.

Do not infer a relationship from coordinate adjacency.

## 9. Scope, viewpoint, view, and context

These are explicit qualifiers, not hidden dimensions:

- **Scope:** what is included/excluded (system boundary, domain coverage, time horizon, scale).
- **Stakeholder concern:** the question or risk a model must address.
- **Viewpoint:** conventions and model kinds used to address one or more concerns.
- **View:** a particular representation produced under a viewpoint.
- **Context:** operating environment, assumptions, constraints, and conditions.
- **Metadata:** ownership, lifecycle, confidence, tags, and descriptive properties.

One entity can be presented in multiple views without duplicating its identity.

## 10. Invariants

1. Stable identity is independent of address.
2. A coordinate is semantic and view-relative, not Cartesian.
3. Module is not synonymous with domain.
4. Scope is not depth.
5. Relationships are explicit graph edges.
6. Coordinates do not imply dependency, containment, similarity, or sequence.
7. Time validity is distinct from record time.
8. Canonical source records remain authoritative; indexes and visualizations are derived.
9. Every externally sourced assertion must retain provenance and rights/attribution metadata.
10. Status is never promoted by visualization or successful parsing alone.

## 11. Open design questions

- Whether Y should be a first-class EKTA module registry or remain a stable ID referenced by entity records.
- Whether the decomposition relation should add a canonical inverse predicate CONTAINS, or keep PART_OF as the sole canonical direction.
- Whether views should be first-class entities in the schema.
- Whether full bitemporal querying is justified for the first runtime integration.
- Whether JSON-LD/RDF export is needed now or only after the internal model stabilizes.
