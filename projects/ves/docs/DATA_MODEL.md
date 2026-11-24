# VES Data Model and Interchange Contract

## Canonical objects
- Project: identity, schema version and metadata.
- Entity: typed engineering concept, component or resource.
- Relationship: directed typed link between entities.
- Board: visual workspace definition.
- Placement: entity reference plus board-local coordinates and card view.
- Requirement, Constraint, Decision, TestCase, TestRun and Evidence: planned typed records; not all are implemented in v0.1.
- Asset: file reference with checksum, MIME type, source and license metadata.

## Identity and separation
Entity IDs are stable and independent of labels, positions and renderers. Renaming does not change identity. Entity = what an object is; Card = how it is presented; Placement = where it appears; Relationship = semantic connection; View = projection.

## Relationships
v0.1 predicates: contains, part_of, connects_to, depends_on, implements, satisfies, verifies, consumes, produces, communicates_with, compatible_with, conflicts_with and derived_from. Predicates are versioned and must be reconciled with EKTA taxonomy before canonical promotion.

## Versioning
Project interchange has schema_version. Incompatible changes require a new major version and migration path. Unknown major versions are rejected. Additive optional fields may be preserved only where semantics are safe.

## Import safety
Import is staged and validated before affecting an existing project. v0.1 import creates a new in-memory project. Future merge operations must use explicit conflict policies: reject, keep-both with new IDs, or field-level merge. Silent overwrite is forbidden.

## Schemas
schemas/project.schema.json defines the initial JSON interchange contract. Python core enforces core invariants; wiring JSON Schema validation into the runtime is a follow-up task.
