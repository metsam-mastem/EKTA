# UPDS–EKTA Integration Index
**Document ID:** UPDS-INDEX-0002  
**Status:** PROPOSED — owner review required  
**Canonical repository:** https://github.com/metsam-mastem/EKTA

## Purpose
This is the entry point for the Universal Project Documentation System (UPDS) proposal as an integrated, separable subsystem of EKTA. It connects project-specific records and lifecycle governance to EKTA's reusable engineering knowledge, without duplicating taxonomy or replacing existing product workspaces.

## Architecture
- [Integration decision](UPDS_EKTA_INTEGRATION_DECISION.md)
- [System architecture](UPDS_EKTA_SYSTEM_ARCHITECTURE.md)
- [Document universe](UPDS_DOCUMENT_UNIVERSE.md)
- [EKTA crosswalk and traceability model](UPDS_EKTA_CROSSWALK.md)
- [Document metadata and template standard](UPDS_DOCUMENT_TEMPLATE_STANDARD.md)
- [Input and artifact model](UPDS_INPUT_AND_ARTIFACT_MODEL.md)
- [Runtime execution blueprint](UPDS_EXECUTION_BLUEPRINT.md)
- [Implementation roadmap](UPDS_IMPLEMENTATION_ROADMAP.md)
- [Project memory and chat independence](UPDS_PROJECT_MEMORY_AND_CHAT_INDEPENDENCE.md)

## Executable foundation
- `schemas/upds-document.schema.json`
- `tools/upds_validation.py`
- `tools/validate_upds.py`
- `tests/test_upds_validation.py`
- `upds/records/EKTA-DOC-000001.yml`

These files form an initial validation foundation. They do not yet constitute a full document registry service or traceability engine.

## User documentation — canonical mainline set
Use [User Documentation Index](../USER_DOCUMENTATION_INDEX.md) as the single user-facing navigation entry. It links:
- Project overview: `docs/PROJECT_OVERVIEW.md`
- Setup and installation: `docs/USER_SETUP.md`, `docs/USER_INSTALLATION.md`
- User manual and workspace guide: `docs/USER_MANUAL.md`, `docs/WORKSPACE_GUIDE.md`
- Input types and intake limits: `docs/INPUT_GUIDE.md`
- Security and staging: `docs/SECURITY_AND_STAGING_MODEL.md`
- Independence and recovery: `docs/INDEPENDENCE_AND_RECOVERY.md`
- Developer/agent onboarding: `docs/AGENT_ONBOARDING.md`

Do not maintain a second competing manual under a parallel path. The older supplemental `docs/USER_GUIDE/` set on the superseded integration branch should be treated as source material for consolidation, not copied as a second authority.

## Canonical memory and handoff
- [Project state](../PROJECT_STATE.md)
- [Active work](../ACTIVE_WORK.md)
- [Decision register](../DECISION_REGISTER.md)
- [Constraints and assumptions](../CONSTRAINTS_AND_ASSUMPTIONS.md)
- [Open issues](../OPEN_ISSUES.md)
- [Evidence index](../EVIDENCE_INDEX.md)
- [Session handoff](../SESSION_HANDOFF.md)
- [Conversation archive and project context](../PROJECT_CONTINUITY/CHAT_SESSION_ARCHIVE_2026-11-24.md)
- [Agent onboarding for chat-independent continuation](../PROJECT_CONTINUITY/AGENT_ONBOARDING.md)
- [Recovery runbook](../PROJECT_CONTINUITY/RECOVERY_RUNBOOK.md)
- [Delivery orchestration plan](../PROJECT_CONTINUITY/ORCHESTRATION_PLAN.md)

## Architecture boundary
EKTA remains the canonical engineering knowledge atlas. UPDS owns project-scoped artifacts: plans, requirements, decisions, change/risk records, evidence, test reports, baselines, releases and handoffs. Shared concepts, taxonomies, reusable methods and relation vocabulary remain governed by EKTA. UPDS must remain extractable behind stable schemas and interfaces.

## Implementation status
| Capability | Status |
|---|---|
| Architecture, catalog, crosswalk and roadmap | DOCUMENTED |
| Base document schema, sample record and validator | IMPLEMENTED — CI verification pending |
| Full registry service/API | NOT IMPLEMENTED |
| Typed project traceability engine | NOT IMPLEMENTED |
| Dashboard and project starter generator | NOT IMPLEMENTED |
| Chat-independent repository handoff design | DOCUMENTED |
| Clean-clone recovery drill and backup restore | NOT RUN |

The current EKTA runtime/workspace capabilities are described in the user documentation. A design document must never be presented as proof of a working feature.


## 14. Runtime registry progress — 2026-11-24
A first read-only UPDS registry slice was added: repository YAML loader, schema validation, duplicate-ID checks, list/get service methods, GET API routes and focused service/API tests. This is not a write-enabled document management system. CI for the current latest head must pass before this code is marked VERIFIED. The next implementation step is controlled draft creation and immutable revision/audit semantics after contract review.
