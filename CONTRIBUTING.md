# Contributing to EKTA

## Read first
Project Charter, Governance, Knowledge Architecture, Concept Schema, and Context Continuity.

## Workflow
Follow [the Knowledge Operating Workflow](docs/KNOWLEDGE_OPERATING_WORKFLOW.md) and the reusable [Knowledge Intake Playbook](workflows/knowledge-intake.md).

1. Identify a knowledge gap or defect and define acceptance criteria.
2. Search the runtime explorer for existing concepts and repository documents before creating a duplicate.
3. Propose taxonomy/schema/architecture changes before making them.
4. Use the appropriate template and stable ID.
5. Add primary sources and separate facts from interpretation.
6. Validate links, territory/domain/layer/type tags, relationships, and required fields.
7. Run repository tests and graph export; report exact commit and CI evidence.
8. Request content and technical review as appropriate.
9. Update maps, continuity, and changelog where relevant.

Use `.github/PULL_REQUEST_TEMPLATE.md` for changes.

## Writing rules
One canonical concept per record. Define acronyms. Preserve standard/API names. Include aliases and disambiguation. State assumptions, version scope, and limitations. Avoid promotional claims. Never say complete, verified, or validated without criteria and evidence.

## Code reuse
Inspect upstream license, dependency tree, maintenance, security advisories, and compatibility before importing code. Prefer links and small attributed examples. Never remove upstream notices.

## Pull request checklist
- [ ] Scope and outcome are clear.
- [ ] No duplicate canonical record exists.
- [ ] Required schema fields are present.
- [ ] Sources are traceable and relevant.
- [ ] Relationships use controlled predicates.
- [ ] Status is accurate.
- [ ] Local links work.
- [ ] Tests run or are marked NOT_RUN.
- [ ] No secrets/private data included.
- [ ] Changelog/maps updated where needed.
