# EKTA Repository Map

```text
EKTA/
├── README.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── CHANGELOG.md
├── LICENSE-STATUS.md
├── docs/                 # charter, architecture, lifecycle, governance, continuity
├── taxonomy/             # domains, layers, knowledge types, relations
├── encyclopedia/
│   ├── concepts/
│   ├── techniques/
│   ├── architectures/
│   ├── components/
│   ├── standards/
│   ├── tools/
│   └── failure-modes/
├── maps/                 # stack, domain, cross-layer and graph maps
├── schemas/              # concept, source, decision and status contracts
├── research/             # research register, literature and source assessment
├── references/           # standards and open-source project indexes
├── decision-lab/
│   ├── RFC/
│   └── ADR/
├── execution-lab/
│   ├── playbooks/
│   ├── checklists/
│   └── workflows/
├── templates/
├── tools/
├── tests/
└── .github/workflows/
```

## Directory rules
- docs: project-level governance, architecture, lifecycle, continuity.
- taxonomy: controlled classification vocabularies.
- encyclopedia: canonical knowledge records.
- maps: human-readable and generated maps.
- schemas: data contracts.
- research: literature discovery and provenance.
- references: curated standards, tools, primary sources.
- decision-lab: proposals and accepted/rejected decisions.
- execution-lab: repeatable procedures.
- templates: reusable artifact forms.
- tools/tests: repository automation and tests.
- .github/workflows: CI gates.

## Naming
Use stable IDs in canonical filenames, e.g. EKTA-CON-000001-runtime.md. IDs are immutable and never recycled. Use lowercase kebab-case for scripts and assets. Do not silently rename a stable ID.
