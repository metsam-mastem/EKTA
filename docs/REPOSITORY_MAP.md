# EKTA Repository Map

```text
EKTA/
├── projects/vel/         # Visual Engineering Language specification, examples, and research
├── README.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── CHANGELOG.md
├── LICENSE-STATUS.md
├── docs/
│   ├── USER_DOCUMENTATION_INDEX.md
│   ├── PROJECT_OVERVIEW.md
│   ├── USER_SETUP.md
│   ├── USER_INSTALLATION.md
│   ├── USER_MANUAL.md
│   ├── INPUT_GUIDE.md
│   ├── INDEPENDENCE_AND_RECOVERY.md
│   ├── TROUBLESHOOTING.md
│   ├── AGENT_ONBOARDING.md
│   └── architecture, governance, continuity, roadmap, handoff
├── taxonomy/             # 26 territories, 25 operational domains, layers, types, relations
├── encyclopedia/         # canonical concepts and engineering knowledge
├── maps/                 # stack, domain, cross-layer and graph maps
├── schemas/              # machine-readable data contracts
├── research/             # literature and source assessment
├── references/           # standards, tools and primary-source indexes
├── decision-lab/         # RFCs and ADRs
├── execution-lab/        # playbooks, checklists and workflows
├── workflows/            # knowledge intake and maintenance procedures
├── runtime/
│   ├── ekta_runtime/      # Python services, search, API and repository facade
│   └── web/               # Persian RTL browser workbench
├── scripts/               # local launch scripts
├── templates/             # canonical record templates
├── tools/                 # validators and graph builder
├── tests/                 # runtime, workspace API and repository tests
└── .github/workflows/     # CI gates
```

## Directory rules
- docs: project, product, user, developer, governance, lifecycle and continuity documentation.
- taxonomy: canonical classification registries.
- encyclopedia: canonical knowledge records; IDs are stable.
- maps: human-readable and generated knowledge maps.
- schemas: machine-readable contracts.
- research: literature discovery, source metadata and provenance.
- references: curated standards, tools and primary sources.
- decision-lab: proposals and accepted/rejected decisions.
- execution-lab: repeatable procedures and verification.
- workflows: intake, review, publishing and maintenance procedures.
- runtime: local-first services, API and browser explorer.
- scripts: local start and maintenance scripts.
- templates: reusable record and work-item forms.
- tools/tests: automation, validators and test coverage.
- .github/workflows: continuous integration gates.

## Naming
Use stable IDs in canonical filenames, e.g. EKTA-CON-000001-runtime.md. IDs are immutable and never recycled. Use lowercase kebab-case for scripts and assets. Do not silently rename a stable ID.

## VEL files
- projects/vel: VEL specification, card catalog, research register, roadmap, and example models.
- schemas/vel-model.schema.json: machine-readable VEL model contract.
- runtime/ekta_runtime/vel.py: local semantic validator and DOT exporter.
- tests/test_vel.py: VEL conformance and regression tests.
- tools/validate_vel.py: schema and semantic validation command.
- docs/VEL_INTEGRATION.md: boundary and integration policy between EKTA and VEL.
