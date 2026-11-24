# USDO — Universal Structural & Dimensional Ontology

**EKTA extension · Initial foundation · Status: PROPOSED**

USDO is a cross-domain descriptive model for representing an entity or system through independent, explicitly typed facets. It extends EKTA without replacing its approved engineering territories, operational domains, engineering layers, knowledge types, or relation registry.

## Start here

- [Architecture and terminology](USDO_ARCHITECTURE.md)
- [Cross-facet relation matrix](../maps/USDO_RELATION_MATRIX.md)
- [Controlled facet registry](../taxonomy/usdo-facets.yml)
- [Machine-readable entity schema](../schemas/usdo-entity.schema.json)
- [Canonical CPU example](../examples/USDO_CPU_EXAMPLE.yml)
- [Entity template](../templates/USDO_ENTITY_TEMPLATE.yml)
- [Validator](../tools/validate_usdo.py)
- [Tests](../tests/test_usdo.py)

## Design contract

1. Facets are orthogonal descriptive questions, not a single hierarchy.
2. Macro / meso / micro describe contextual abstraction level, not physical size.
3. Scope, scale, dimension, and layer are separate and non-substitutable.
4. Structure describes composition and responsibilities; topology describes connectivity.
5. A circuit is domain-qualified. A graph cycle is not automatically an engineering circuit.
6. Relations are typed; communication is one subset of relation.
7. Dynamic behavior is separate from static architecture.
8. Evaluation records metrics, constraints, acceptance criteria, methods, and evidence.
9. Unknown values remain explicit; validators do not infer missing facts.
10. Existing EKTA registries remain canonical for their original concerns.

## Maturity boundary

This foundation adds a facet vocabulary, JSON Schema, worked example, template, documentation, and local validator. It does not yet add a runtime API, graph projection, UI, ontology reasoner, automatic classification, or broad domain coverage. Those require separate implementation and acceptance evidence.
