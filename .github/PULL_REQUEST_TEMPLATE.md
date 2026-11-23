## Purpose

What question, capability, or defect does this change address?

## Scope and impact

- [ ] Documentation / knowledge record
- [ ] Taxonomy / ontology
- [ ] Runtime / API
- [ ] User interface / interaction
- [ ] CI / tests / tooling
- [ ] Governance / ADR

## Knowledge integrity

- [ ] Stable IDs are preserved; new IDs are unique.
- [ ] Territory, domain, layer, and knowledge type values exist in canonical registries.
- [ ] Relationship predicates and targets are controlled and traceable.
- [ ] Claims are linked to sources or explicitly marked as uncertain/proposed.
- [ ] Third-party content/license constraints have been reviewed.
- [ ] No content status was promoted merely because this PR merged.

## Verification

- [ ] `python tools/validate_docs.py`
- [ ] `python -m unittest discover -s tests -v`
- [ ] `python tools/build_graph.py`
- [ ] UI/API/browser checks are described below where applicable.

**Verification commit SHA:**

**CI run URL:**

**Outstanding blockers / unresolved links:**

## Review

- [ ] Content/evidence review complete (where applicable).
- [ ] Technical review complete.
- [ ] Taxonomy or architecture decision recorded (where applicable).
