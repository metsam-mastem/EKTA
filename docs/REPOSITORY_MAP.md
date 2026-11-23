# EKTA Repository Map

```text
EKTA/
├── README.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── CHANGELOG.md
├── LICENSE-STATUS.md
├── docs/                 # charter, architecture, lifecycle, governance, continuity
├── taxonomy/             # 26 territories, 25 operational domains, layers, knowledge types, relations
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
├── workflows/            # reusable knowledge intake and maintenance playbooks\n├── runtime/              # Python services, versioned API, and browser workbench\n├── scripts/              # local runtime launchers\n├── templates/
├── tools/
├── tests/
└── .github/workflows/
```

## Directory rules
- docs: project-level governance, architecture, lifecycle, continuity.
- taxonomy: 26 top-level territories plus operational domains, layers, knowledge types, and relations.\n- runtime: local-first application runtime, search services, API, and browser explorer.\n- workflows: operational procedures for intake, review, publishing, and verification.
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


## UPDS integration additions

```text
docs/
├── INTEGRATION/          # UPDS decision, architecture, catalog, crosswalk, memory, templates, roadmap
├── PROJECT_STATE.md
├── DECISION_REGISTER.md
├── ACTIVE_WORK.md
├── OPEN_ISSUES.md
├── CONSTRAINTS_AND_ASSUMPTIONS.md
├── EVIDENCE_INDEX.md
└── SESSION_HANDOFF.md
```

These additions are proposed integration documentation and repository-native continuity registers. See [UPDS Integration Index](INTEGRATION/UPDS_INTEGRATION_INDEX.md).
