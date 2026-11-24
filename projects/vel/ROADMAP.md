# VEL Roadmap

## Current increment: v0.1.0 foundation

Status: PROPOSED baseline with an initial reference implementation.

Delivered in this increment:
- Specification and JSON Schema.
- Card and connector vocabulary.
- Python semantic validator.
- DOT export.
- Example architecture.
- Unit tests and EKTA integration notes.

Not delivered:
- Visual canvas, physical card print package, camera scanning, QR recognition, adapters to external modeling standards, collaboration, or code generation.

## Next increments

### v0.2 — Model and schema hardening
- Add JSON Schema validation to CI.
- Define extension namespaces and domain profiles.
- Define evidence references, assumptions, decisions, and requirement traceability.
- Add canonical serialization and model diff/patch format.
- Add conformance fixtures and negative test corpus.

### v0.3 — Minimal digital canvas
- Prototype React Flow custom cards and typed ports.
- Persist the exact VEL JSON model.
- Add import/export and deterministic IDs.
- Add auto-layout via ELK after baseline graph editing works.
- Support desktop/mobile responsive layout and keyboard accessibility.

### v0.4 — Physical card kit
- Printable entity cards, connector strips, and state tokens.
- QR identity markers and a documented card revision.
- Camera capture and manual correction workflow.
- Do not claim OCR accuracy until measured against a labeled test set.

### v0.5 — Viewpoints and adapters
- Software architecture profile.
- System/hardware profile.
- Workflow/automation profile.
- CALM, D2, C4/Structurizr and SysML v2 mapping experiments.
- Adapter conformance and loss-report tests.

### v0.6 — Engineering traceability
- Requirement-to-node and test-to-requirement links.
- Evidence registry and verification state rules.
- Change impact analysis and model diff.
- Review/approval workflow.

### v1.0 — Stable language release
Requires:
- Published compatibility policy.
- Schema and parser conformance suite.
- Documented adapter loss semantics.
- Security review of import/export.
- Usability testing with physical and digital workflows.
- Versioned reference implementation and migration guide.

## Delivery gates

Each increment follows: Define → Implement → Test → Review → Document → Retest. Statuses are PASS, FAIL, NOT RUN, or BLOCKED. A feature is not called implemented or verified without corresponding code and evidence.
