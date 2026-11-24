# USDO Cross-Facet Relation Matrix

This matrix describes interactions among facets. It is not a taxonomy and does not imply that one facet is a subtype of another.

| Source facet | Related facet | Relation / question | Example |
|---|---|---|---|
| Ontology | Classification | classified-as | A CPU is a digital processor |
| Ontology | Scope | scoped-by | A model describes a CPU family, not every CPU |
| Dimension | Evaluation | measured-by | Latency measured in milliseconds |
| Dimension | Scale | resolved-at | Time dimension sampled at 1 ms resolution |
| Scope | Evaluation | bounds-validity | A benchmark applies only under declared workload conditions |
| Layer | Architecture | realizes-responsibility | Runtime layer owns process lifecycle |
| Layer | Relation | depends-on | Application layer depends on service layer |
| Architecture | Topology | contains-connectivity | Modular structure has a star-shaped internal bus |
| Topology | Circuit | supports-path | Graph topology contains a signal path |
| Circuit | Dynamics | carries-flow | Control loop carries measured and control signals |
| Relation | Dynamics | triggers-or-constrains | Event relation causes a state transition |
| Dynamics | Evaluation | observed-by | State transitions are checked by tests |
| Scale | Architecture | changes-decomposition | Different scale may require different decomposition |
| Scope | Architecture | constrains-view | A bounded architecture description selects relevant views |

## Core distinctions

- HAS_DIMENSION does not mean PART_OF.
- LOCATED_IN_LAYER does not mean IS_A.
- WITHIN_SCOPE does not mean DEPENDS_ON.
- CONNECTED_TO does not imply semantic dependency.
- CIRCUIT_OF must identify a domain-qualified circuit kind.
- FEEDBACK_TO is directed behavior; do not infer it from a generic undirected graph cycle.
- MEASURED_BY must identify a metric and, where applicable, unit and measurement conditions.

## Modeling guidance

1. Store facet values in their own schema properties.
2. Use graph edges only for explicit relations between identifiable entities.
3. Use local attributes for dimensions, metrics, states, or components when they are not independently addressable entities.
4. Promote a value to a first-class entity when it has its own identity, lifecycle, provenance, or relationships.
5. Preserve direction and evidence status for uncertain claims.
6. Never infer missing relations from naming similarity.
