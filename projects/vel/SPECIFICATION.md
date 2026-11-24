# VEL Specification 0.1.0

**Status:** Proposed baseline  
**Normative language:** MUST, MUST NOT, SHOULD, MAY are used in their conventional requirements sense.

## 1. Purpose

VEL defines a visual engineering language that can be authored through physical cards, a digital canvas, structured JSON, or an AI-assisted interaction. All authoring modes MUST resolve to the same canonical model contract.

## 2. Model envelope

A VEL document MUST contain:
- `schema_version`: version of the VEL interchange schema.
- `model_id`: stable model identifier.
- `name`: human-readable model name.
- `revision`: model revision.
- `status`: DRAFT, PROPOSED, APPROVED, IMPLEMENTED, VERIFIED, BLOCKED, or DEPRECATED.
- `nodes`: engineering entities.
- `connections`: typed relationships between ports.

A document MAY include `groups`, `layers`, `annotations`, and `metadata`.

## 3. Node model

Each node has:
- `id`: unique stable identifier within the model.
- `kind`: controlled or profile-defined entity kind.
- `label`: display label.
- `status`: DRAFT, PROPOSED, APPROVED, IMPLEMENTED, VERIFIED, BLOCKED, or DEPRECATED.
- `ports`: declared interfaces.
- optional `layer`, `description`, `ekta_refs`, and `properties`.

Node identity MUST NOT depend on its screen position, color, or label. Renaming a node MUST preserve its ID.

## 4. Port model

Each port has:
- `id`: unique within its node.
- `name`: display label.
- `direction`: IN, OUT, or INOUT.
- `channels`: one or more accepted semantic channel types.

Initial channel vocabulary:
- DATA
- CONTROL
- EVENT
- POWER
- SIGNAL
- MECHANICAL
- NETWORK
- DEPENDENCY
- MATERIAL
- FLUID
- THERMAL

Domain profiles MAY extend this vocabulary using namespaced values. A profile MUST document the meaning and compatibility rules of every extension.

## 5. Connection model

A connection has:
- `id`: stable identifier.
- `kind`: semantic channel type.
- `source`: source node and port.
- `target`: target node and port.
- `status`: DRAFT, PROPOSED, APPROVED, IMPLEMENTED, VERIFIED, BLOCKED, or DEPRECATED.
- optional `label`, `description`, and `properties`.

A valid connection MUST reference existing nodes and ports. Source direction MUST be OUT or INOUT. Target direction MUST be IN or INOUT. Its `kind` MUST be declared by both endpoint ports.

A visual line without a semantic connection kind is an annotation, not a valid engineering connection.

## 6. Groups and layers

Groups provide visual or logical containment. Group membership MUST reference existing node IDs. A node MAY belong to multiple non-exclusive views; the canonical model MUST distinguish visual grouping from ownership or runtime containment.

Layers are labels or references to a domain profile. A layer MUST NOT be interpreted as execution order unless the profile explicitly defines that meaning.

## 7. Status and evidence

Status values describe lifecycle state, not confidence:
- DRAFT: local working material.
- PROPOSED: submitted for review.
- APPROVED: explicitly accepted by an authorized reviewer.
- IMPLEMENTED: implementation exists and is linked.
- VERIFIED: specified verification passed with evidence.
- BLOCKED: progress is blocked by a recorded reason.
- DEPRECATED: no longer recommended; retained for traceability.

A model status MUST NOT automatically promote its nodes or connections. VERIFIED requires evidence references and a defined verification scope. The initial validator checks structural semantics; it does not prove implementation correctness.

## 8. Ambiguity and unknowns

Unknown information MUST be represented as an explicit annotation or an unresolved decision record. Consumers MUST NOT infer a missing connection, protocol, direction, unit, or requirement as fact.

Suggested annotation states: QUESTION, ASSUMPTION, CONFLICT, TODO, RISK, DECISION.

## 9. Interchange and determinism

- UTF-8 JSON is the canonical interchange format for v0.1.
- Consumers SHOULD preserve unknown extension properties.
- Producers SHOULD emit deterministic JSON (stable IDs and stable ordering).
- A renderer MUST NOT mutate model semantics when changing layout.
- Adapters MUST report lossy mappings and unsupported constructs.

## 10. Security

VEL files are data, not executable instructions. Importers MUST NOT execute scripts embedded in labels, properties, SVG, or metadata. External URLs and file references MUST be treated as untrusted input. The initial Python validator performs no network access and no code execution.

## 11. Compatibility

Schema version changes follow semantic versioning:
- PATCH: clarifications or backward-compatible corrections.
- MINOR: backward-compatible optional fields or vocabulary additions.
- MAJOR: incompatible structural or semantic changes.

Domain profiles MUST declare the VEL schema range they support.

## 12. Non-goals for 0.1

The baseline does not include a browser editor, multi-user collaboration, real-time sync, OCR, QR scanning, image-to-graph inference, code generation, runtime execution, or automatic architecture approval.
