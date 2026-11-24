# VEL Integration with EKTA

## Boundary

EKTA is the canonical engineering knowledge atlas. VEL is a visual engineering language and model interchange contract.

EKTA stores definitions, standards, techniques, tools, source provenance, decisions, and evidence. VEL stores a particular model: nodes, ports, connections, groups, layers, states, and references to EKTA knowledge.

## Integration contract

- VEL MAY reference EKTA records using stable IDs in `ekta_refs`.
- VEL MUST NOT copy the full EKTA concept definition into a VEL node.
- EKTA records remain authoritative for knowledge definitions and source provenance.
- VEL model files are stored under `projects/vel/`; the validator implementation is in `runtime/ekta_runtime/vel.py`.
- Future EKTA UI components may render VEL files, but the VEL schema remains independently versioned.
- Changes to either contract require a documented compatibility decision.

## VES relationship

The repository contains a branch named `project/ves-foundation-v0.1`. During the 2026-11-24 inspection, that branch was observed at the same commit as `main`; no VES-specific implementation was found in the inspected main tree. Therefore this integration does not assume VES and VEL are synonyms or merge their scopes. A future ADR must define whether VES is a broader environment, a product shell, or a separate system that consumes VEL.

## Operational safeguards

- No existing EKTA canonical concept records are rewritten by VEL.
- No external source code is vendored by this contribution.
- No database, cloud service, or paid dependency is introduced.
- The first VEL validator is local and deterministic.
- Imported model files are treated as data and are never executed.
