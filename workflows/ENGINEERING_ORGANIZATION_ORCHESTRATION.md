# Engineering Organization Development Orchestration

**Workstream:** EKTA engineering knowledge organization  
**Status:** PROPOSED / PR #22  
**Branch:** knowledge/engineering-organization-v1  
**Execution model:** parallel discovery and drafting; controlled serial integration.

## 1. Objective

Expand the engineering organization model into a source-grounded, machine-checkable and operationally useful EKTA knowledge layer without creating a parallel project or replacing canonical taxonomy.

## 2. Workstreams

| Lane | Scope | Deliverables | Dependency |
|---|---|---|---|
| A — Taxonomy integration | Crosswalks, axis boundaries, stable IDs, coverage gaps | Canonical-compatible registries, mapping tests | Existing EKTA taxonomy |
| B — Terminology and ontology | Definitions, synonyms, boundaries, typed relations | Concept candidates, glossary, ontology review | A |
| C — Standards and sources | Primary-source research, editions, authority, provenance | Source records, standards crosswalk, evidence notes | B |
| D — Documentation architecture | Role sets, document types, Diátaxis, templates | User/developer/operator/engineering documentation model | B |
| E — Lifecycle and traceability | Lifecycle activities, gates, outputs, trace links | Process maps, acceptance and evidence contracts | A, D |
| F — Tooling and validation | JSON Schema, deterministic validators, tests, CI | Repeatable validation and generated reports | A-E |

Lanes A-D can perform bounded research in parallel. E can draft against current models while recording assumptions. F integrates only after the relevant contracts stabilize.

## 3. Integration sequence

1. Read current repository governance, taxonomy, schemas, handoff, and CI.
2. Freeze the scope and mark all new classification constructs as views until approved.
3. Draft independent workstream outputs with source and confidence metadata.
4. Reconcile names, definitions, IDs, and relationship semantics.
5. Validate registry references, schemas, links, duplicate IDs, and provenance.
6. Review changed files and inspect generated graph/runtime impact.
7. Open or update one integration PR; do not create parallel canonical branches for the same files.
8. Merge only after CI passes and maintainer review accepts the scope.
9. Record the resulting commit and next work item in the handoff.

## 4. Parallel execution contract

- Parallelize research and independent document drafting, not writes to the same file.
- Assign one owner per canonical file or registry during a work batch.
- Do not run concurrent updates against the same Git path.
- Keep branch names scoped to one coherent workstream.
- Integrate shared taxonomy and schema changes serially.
- Preserve source URLs, edition/date, access date, claim supported, limitations, and confidence.
- Separate source-derived facts from synthesis and proposed EKTA conventions.

## 5. Work item contract

Every work item must include:
- objective and explicit non-goals;
- affected EKTA paths;
- source set and provenance;
- expected output and acceptance criteria;
- risks and dependencies;
- validation commands;
- status: PASS, FAIL, NOT_RUN, or BLOCKED;
- commit/PR evidence and next action.

## 6. Quality gates

- Taxonomy: no duplicate IDs, no unknown canonical references, no unapproved axis changes.
- Ontology: every relation has a defined direction and meaning; avoid ambiguous generic edges.
- Sources: no unsupported normative claim; verify standard edition and issuing body.
- Documentation: audience, purpose, authority, status, and lifecycle are explicit.
- Lifecycle: plans and artifacts are not confused with executed work or evidence.
- Code: validators are deterministic, tests cover failure modes, CI invokes the validators.
- Governance: no license or standards-conformance claims beyond available evidence.

## 7. Current batch status

| Item | Status | Evidence |
|---|---|---|
| Handwritten note transcription and uncertainty record | PROPOSED | research/HANDWRITTEN_NOTE_ANALYSIS_2021.md |
| 14-area crosswalk | PROPOSED | taxonomy/ENGINEERING_ORGANIZATION_VIEW.json |
| Terminology boundaries | PROPOSED | docs/ENGINEERING_TERMINOLOGY.md |
| Documentation architecture | PROPOSED | docs/ENGINEERING_DOCUMENTATION_SYSTEM.md |
| Lifecycle crosswalk | PROPOSED | docs/ENGINEERING_LIFECYCLE_CROSSWALK.md |
| Validator and regression tests | Added to branch; CI pending | tools/validate_engineering_organization.py and tests/test_engineering_organization.py |
| Integration | OPEN | Pull request #22 |

## 8. Next prioritized batch

1. Review the 14-area crosswalk with maintainers; do not promote it to canonical taxonomy without approval.
2. Build an evidence-backed concept inventory for each existing territory, beginning with software, systems, hardware/electronics, networking, automation/robotics, manufacturing, security/safety, and documentation/governance.
3. Create a controlled term register for language, library, framework, SDK, IDL, API, ABI, runtime, toolchain, package, module, plugin, and middleware.
4. Add architecture-description concepts and viewpoint/view/model-kind distinctions.
5. Build document-type and lifecycle-artifact schemas only after the terminology and ownership model are reviewed.
6. Expand source evaluation and standard applicability records; never reproduce normative copyrighted text.

## 9. Continuity and execution limits

This file is the durable orchestration contract. It does not imply that agents continue running after a chat turn or that work proceeds indefinitely in the background. Each execution batch must end with inspectable commits, CI results, blockers, and a next action. A future session should resume from this file and the current Git branch/PR state, not from chat recollection alone.
