# Engineering Documentation System

## 1. Purpose

Documentation is an engineered information system. Each information product has an intended audience, purpose, authority, lifecycle, owner, source basis, and change process.

Distinguish knowledge records; engineering information products; management artifacts; user assistance; operational instructions; and generated projections such as indexes, maps, API docs, and graph exports.

## 2. Documentation dimensions

| Dimension | Values / examples |
|---|---|
| Audience | executive, sponsor, product, system engineer, architect, developer, tester, operator, maintainer, end user, auditor, supplier |
| Purpose | authorize, decide, specify, explain, teach, instruct, reference, verify, report, operate, recover |
| Authority | normative, contractual, approved policy, approved baseline, informative, working draft, generated |
| Lifecycle | discovery, feasibility, requirements, architecture, design, implementation, verification, transition, operations, maintenance, retirement |
| Scope | organization, portfolio, program, project, product, system, subsystem, component, service |
| State | DRAFT, PROPOSED, REVIEWED, APPROVED, BASELINED, SUPERSEDED, DEPRECATED, ARCHIVED |
| Provenance | author, source references, generated-from revision, tool/version, review evidence |

These are document metadata dimensions, not additions to EKTA's canonical concept classification axes.

## 3. Document families

### Governance and strategy
Vision, mission, objectives, strategy, governance model, policies, roles and decision rights, charter, business case, portfolio, roadmap, compliance and audit records.

### Requirements and specification
Stakeholder and user needs, system/software requirements, interface and data specifications, constraints, assumptions, acceptance criteria, requirements traceability.

### Architecture and design
Architecture description and viewpoints, context/structural/behavioral/deployment/data/security/operational views, ADRs, design descriptions, models, interface contracts, bills of materials.

### Implementation and configuration
Source code, build configuration, dependency manifests and lockfiles, configuration baselines, API/IDL/schema definitions, packaging, signing, release and migration instructions.

### Verification, validation and assurance
Verification strategy and plans, test specifications/cases/procedures/reports, inspection and review records, security assessments, threat models, safety analyses, defect/deviation/waiver/corrective-action records, acceptance evidence.

### Delivery and transition
Release plan, release notes, deployment and installation guides, migration and rollback plans, training, handover, acceptance and delivery records.

### Operations and maintenance
Service catalog, operational procedures, runbooks, monitoring definitions, incident playbooks, backup/restore, continuity and disaster recovery, troubleshooting, repair, upgrades, compatibility, end-of-support and retirement plans.

### User and developer assistance
Tutorials, how-to guides, reference, explanations, user manual, role-specific guides, developer onboarding, contribution guide, troubleshooting and FAQ.

### Research and knowledge
Source register, source assessments, research briefs, literature reviews, technical notes, glossary, ontology, taxonomy, concept records, lessons learned and post-incident reviews.

## 4. Minimum document metadata

For durable documents, record as applicable:
- stable document ID;
- title and document type;
- status and revision;
- owner and intended audience;
- scope and applicable system/version;
- created/updated/approved dates;
- source references and provenance;
- related requirements, concepts, decisions, components, tests and releases;
- review/approval record;
- supersedes/superseded-by links.

Do not invent approvals, owners, signatures, or baselines. Missing values remain explicit.

## 5. Role-oriented documentation sets

| Role | Minimum useful set |
|---|---|
| Executive / sponsor | vision, business case, charter, roadmap, risk and status report |
| Product manager | product strategy, user needs, requirements, roadmap, release plan, metrics |
| System engineer | stakeholder needs, requirements, architecture, interfaces, verification and validation evidence |
| Architect | architecture description, viewpoints, ADRs, quality scenarios, constraints, dependency map |
| Developer | developer guide, code conventions, API/IDL reference, build/test instructions, contribution workflow |
| Tester / QA | test strategy, test plan, test cases, environments, defect process, evidence rules |
| Operator / SRE | deployment guide, runbooks, monitoring, incident and recovery procedures |
| Maintainer | architecture/design, dependency inventory, troubleshooting, migration and maintenance instructions |
| End user | setup, installation, tutorial, task guides, user manual, troubleshooting |
| Auditor / assessor | requirements baseline, standards applicability, traceability, approvals, test and compliance evidence |

## 6. Documentation lifecycle

Draft → technical review → editorial/accessibility review → approval when required → baseline/release → maintenance → supersession or archive.

For continuously updated documentation, review and version it alongside the product. A document is not authoritative merely because it exists in the repository.

## 7. Quality checks

- Is the audience explicit?
- Does the title accurately state the purpose?
- Are terms consistent with the EKTA glossary?
- Are requirements testable and unambiguous?
- Are architecture views tied to stakeholder concerns?
- Are examples versioned and executable where claimed?
- Are links and references valid?
- Are normative claims supported by an authoritative source?
- Are limitations, assumptions, and known gaps stated?
- Is the document status accurate?
- Can a new reader complete the intended task without chat history?

## 8. Relationship to Diátaxis

Diátaxis organizes technical assistance by reader need (tutorial, how-to, reference, explanation). EKTA's role-based documentation sets organize by audience and responsibility. These dimensions intersect but are not substitutes. A developer may need a tutorial, reference, and explanation; a user manual may contain how-to content while remaining a role-oriented product manual.
