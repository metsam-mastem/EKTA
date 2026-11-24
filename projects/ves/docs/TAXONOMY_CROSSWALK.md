# VES ↔ EKTA Taxonomy Crosswalk

**Verification date:** 2026-11-24  
**Status:** Identifier membership verified against current EKTA registries; semantic approval remains subject to EKTA governance.

## Purpose
Map VES project classifications to existing EKTA taxonomy identifiers without creating parallel or invented EKTA identifiers.

## Verified taxonomy axes
- 24 relevant territories from the current 26-territory navigation registry.
- 22 relevant domain identifiers; the domain registry currently labels its records as proposed.
- All 10 registered engineering layers.
- 20 existing knowledge-type identifiers.
- 13 VES relation mappings, with direct, inverse, approximate or no-direct-equivalent semantics.

## Important semantic constraints
1. Registry membership is not equivalent to approval. Domain records in EKTA currently carry status proposed.
2. VES contains and part_of have inverse direction.
3. VES verifies maps to EKTA VERIFIED_BY only after direction is interpreted from the participating entity types.
4. communicates_with is only an approximate mapping to CONNECTS_TO; preserve the original VES predicate as a qualifier.
5. satisfies, compatible_with and conflicts_with have no exact EKTA predicate in the current registry. Do not coerce them into RELATED_TO or another relation.
6. Never write VES-specific predicates into EKTA canonical taxonomy automatically.

## Machine-readable mapping
The exact IDs and relation mappings are maintained in integration/ekta-taxonomy-crosswalk.json. tests/test_crosswalk.py checks every ID against the current YAML registries during EKTA CI.

## Governance
Any change to this mapping requires a reviewed PR, registry validation and an explicit semantic decision record. The crosswalk does not mutate EKTA taxonomy.
