# EKTA Taxonomy Model

## Two-level classification — not two competing lists

EKTA separates two classification purposes:

1. **Engineering Territories (26):** the approved top-level navigation and portfolio map. These are the major engineering territories a user browses from the home surface.
2. **Operational Domains (25):** more granular tags used to classify concepts, implementations, techniques, sources, and workflows. A domain may contribute to more than one territory.

The authoritative registries are:
- `taxonomy/territories.yml` — 26 top-level territories and their current domain mappings.
- `taxonomy/domains.yml` — operational domain identifiers.
- `taxonomy/layers.yml` — engineering stack layers.
- `taxonomy/knowledge-types.yml` — knowledge record types.
- `taxonomy/relations.yml` — controlled graph predicates.

Territory membership is therefore derived from a concept's domain tags through the explicit `domain_ids` mappings in `territories.yml`. An empty mapping means the territory exists as an approved navigation node but does not yet have a narrower operational domain mapping. It does not mean the territory is out of scope.

## Classification rules

- Domains, layers, and knowledge types are independent axes.
- Concepts may have multiple domain, layer, and territory memberships.
- Do not infer a territory when no explicit domain mapping or record-level mapping exists.
- New domain identifiers require an update to the domain registry and tests.
- New territory changes require an ADR or maintainer review because the 26-node map is an approved top-level product taxonomy.
- Stable IDs are machine-facing; labels may be revised without changing IDs.

## Current counts

- Engineering territories: 26
- Operational domain tags: 25
- Engineering layers: 10
- Relation predicates: 20
- Knowledge types: 30

Counts are generated from the canonical YAML registries and should be kept in CI, not manually represented as a claim of content coverage.
