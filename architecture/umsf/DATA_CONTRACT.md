# UMSF Data Contract 0.1

## Canonical JSON shape

The contract is intentionally small and implementation-neutral. The JSON Schema at `schemas/umsf.schema.json` validates the structural shape. Cross-record rules (unique IDs, valid layer references, relation endpoints, time interval ordering) are enforced by the Python validation core and, in a later phase, by repository-wide validators.

```json
{
  "schema_version": "0.1.0",
  "model_id": "EKTA-UMSF-MODEL-0001",
  "root_entity_id": "EKTA-EXAMPLE-SYSTEM-0001",
  "view_id": "EKTA-UMSF-VIEW-EXAMPLE-0001",
  "entities": [
    {
      "id": "EKTA-EXAMPLE-SYSTEM-0001",
      "type": "system",
      "name": "Example System",
      "addresses": [
        {
          "x_layer_id": "application-agent",
          "y_module_id": "EKTA-EXAMPLE-MODULE-0001",
          "z_depth": 0,
          "valid_from": "2026-01-01T00:00:00Z",
          "valid_to": null
        }
      ],
      "metadata": {
        "domains": ["software-engineering"],
        "scope": "Illustrative example only"
      }
    },
    {
      "id": "EKTA-EXAMPLE-MODULE-0001",
      "type": "module",
      "name": "Identity Module",
      "addresses": []
    }
  ],
  "relationships": [
    {
      "source_id": "EKTA-EXAMPLE-SYSTEM-0001",
      "predicate": "PART_OF",
      "target_id": "EKTA-EXAMPLE-MODULE-0001",
      "status": "PROPOSED"
    }
  ],
  "provenance": []
}
```

The example is illustrative and does not claim that its sample IDs exist in EKTA's canonical encyclopedia. The relationship direction in production records must follow the documented predicate semantics; the example should be read as a schema illustration only.

## Field semantics

| Field | Required | Meaning |
|---|---:|---|
| schema_version | yes | Contract version |
| model_id | yes | Stable ID for this model |
| root_entity_id | yes | Root entity for the decomposition view |
| view_id | yes | Stable ID for the view |
| entities | yes | Entity records |
| entity.id | yes | Stable identity, not derived from coordinates |
| entity.type | yes | Controlled or documented entity type |
| entity.name | yes | Canonical display name |
| addresses | yes | Zero or more semantic addresses |
| x_layer_id | yes per address | EKTA layer ID |
| y_module_id | yes per address | Stable module ID |
| z_depth | yes per address | Non-negative view-relative depth |
| valid_from | yes per address | ISO 8601 time with timezone |
| valid_to | no | Exclusive end of validity |
| metadata | no | Scope, domain tags, ownership, constraints, etc. |
| relationships | yes | Explicit typed graph edges |
| provenance | no | Source and derivation records |

## Validation layers

1. JSON Schema: required fields, primitive types, arrays, minimum depth, and timestamp strings.
2. Semantic validation: ISO-8601 timezone presence, interval ordering, unique IDs, known layer IDs, root existence, and relation endpoints.
3. Governance validation: controlled predicates, source/provenance references, status policy, and license/attribution checks.
4. Runtime validation: deterministic loading and no silent normalization or evidence-status promotion.

## Example coordinate interpretation

`(application-agent, EKTA-EXAMPLE-MODULE-0001, 2, 2026-01-01T00:00:00Z…)` means: in this declared view, this entity is assigned to the application/agent architectural layer, associated with the identified functional module, appears at decomposition depth 2 relative to the declared root, and is valid from the given time. It does not mean the module is two physical units away or that the entity is two levels more complex in every context.
