# VEL — Visual Engineering Language

**Version:** 0.1.0  
**Status:** PROPOSED / implementation foundation  
**Home:** EKTA `projects/vel/`  
**Canonical code:** `runtime/ekta_runtime/vel.py`

VEL is a human-readable and machine-processable visual language for describing engineering systems with cards, typed ports, connectors, groups, layers, states, and evidence. It is designed to bridge physical card layouts, digital canvases, structured architecture models, and AI-assisted engineering workflows.

VEL is a language and interchange contract, not merely a diagramming UI. Its canonical representation is JSON. A renderer is a view of that model; it is not the source of truth.

## Relationship to EKTA

- EKTA remains the canonical engineering knowledge atlas and source of domain knowledge.
- VEL is a visual modeling language and model interchange layer.
- VEL records may reference EKTA concepts by stable IDs; VEL does not duplicate EKTA definitions.
- Integration is through explicit references and adapters, not by merging the projects.
- Existing `project/ves-foundation-v0.1` branch was observed during repository inspection. It currently points to the same commit as `main`; no assumption is made that VES and VEL are identical. Any future VES relationship requires an explicit architecture decision.

## First increment

This contribution establishes:
1. A versioned JSON meta-model and JSON Schema.
2. A Python semantic validator for IDs, ports, directions, and connector compatibility.
3. A DOT exporter for inspection and downstream visualization.
4. A minimal local-AI-workstation example.
5. Documentation for the visual grammar, card catalog, research references, adapters, and roadmap.
6. Automated tests.

It does **not** claim to provide a graphical editor, camera recognition, QR scanning, automatic code generation, or production-grade adapter integrations.

## Quick start

From the EKTA repository root:

```bash
python tools/validate_vel.py projects/vel/examples/local-ai-workstation.json
python -m unittest tests.test_vel -v
```

The validator uses the existing EKTA runtime dependencies. The core semantic checks in `ekta_runtime.vel` use only the Python standard library.

## Core principles

- One canonical model, multiple synchronized views.
- Every node and connector has a stable identity.
- Every connector has a semantic type.
- Ports define direction and accepted channels.
- Ambiguity is represented explicitly; it is not silently guessed.
- Model status and verification evidence are separate.
- No status is promoted without evidence and an authorized review.
- External project integrations are adapters; VEL owns its own model contract.

## Documents

- [Specification](SPECIFICATION.md)
- [Card catalog](CARD_CATALOG.md)
- [Research and adapters](RESEARCH_AND_ADAPTERS.md)
- [Roadmap](ROADMAP.md)
- [Integration with EKTA](../../docs/VEL_INTEGRATION.md)
- [Example model](examples/local-ai-workstation.json)
- [JSON Schema](../../schemas/vel-model.schema.json)
