# EKTA User Manual
**Document ID:** EKTA-USER-MANUAL-0001 | **Status:** DOCUMENTATION BASELINE
**Baseline:** local read-only Search & Explore Workbench v0.2, as described by repository documentation.

## 1. Start and stop
Start with the platform script in the root README and keep its terminal open. Browse to http://127.0.0.1:8000. Stop with Ctrl+C. If startup fails, inspect terminal output before retrying.

## 2. Recommended engineering workflow
1. Define the engineering question and decision context.
2. Search the atlas and inspect candidate concepts/documents.
3. Check identity, status, taxonomy, provenance and evidence.
4. Follow typed relations to dependencies, implementations and methods.
5. Compare alternatives and create a decision record when a consequential choice is needed.
6. Convert the chosen option into tasks, procedures and acceptance criteria.
7. Capture tests, measurements, source links and deviations.
8. Curate reusable findings into canonical knowledge through reviewed Git changes.

Steps 4–8 describe the intended work practice. Runtime v0.2 is documented as read-only; do not assume the UI can edit records or execute projects.

## 3. Search inputs
The root README documents these forms:
| Input | Meaning |
|---|---|
| runtime engine | all terms matched across indexed fields |
| #runtime | hashtag/tag-derived match |
| "workflow runtime" | exact phrase |
| territory:software-engineering | filter by canonical territory |
| domain:software-engineering | filter by operational domain |
| layer:platform-runtime | filter by engineering layer |
| type:concept | filter by knowledge type |
| status:PROPOSED | filter by maturity |
| kind:document | result family such as concept/document/taxonomy/schema |
| id:EKTA-CON-000001 | stable ID lookup |

Multiple words are documented as AND-matched. Example:
~~~text
runtime territory:software-engineering layer:platform-runtime status:PROPOSED
~~~
Check actual runtime behavior for case handling and escaping.

## 4. Input families and submission
The exact ingestion UI and automatic import pipeline are not established. Until a specific importer exists, submit material as a reviewed Git change or reference it from a research/evidence record.

- **Text:** definitions, notes, requirements, observations, procedures and transcripts. Preserve original evidence; separate quotation from interpretation; record source, author and date.
- **Structured data:** YAML, JSON, CSV, tables and schema records. Preserve field names, units, encoding, null semantics and provenance; validate before commit.
- **Code/repositories:** record URL, commit/tag, path, license, language, build steps and test results. A URL alone does not prove build or execution.
- **Documents/publications:** PDF, DOCX, Markdown, HTML and standards. Capture title, author, publisher, date, revision, URL, page/section, license and claims. Do not reproduce copyrighted content without permission.
- **Images/diagrams:** retain original resolution and labels; record creator, date, context, units and textual description. Keep interpretation separate from original.
- **Audio/video:** record creator, origin, date, duration, language, transcript method and timestamped segments. Transcript is a derived artifact.
- **CAD/EDA/3D/CAE:** preserve native format, tool/version, units, coordinate system, dependencies, export settings and validation state.
- **Test/measurement evidence:** include procedure, setup, equipment/calibration, environment, inputs, expected/actual results, units, raw data, logs, operator, timestamp and deviations.
- **Links/external sources:** record canonical URL, retrieval date, publisher, version, section and access/license notes.
- **Conversation/AI output:** treat as unverified. Identify model/tool and date, verify against primary sources, and mark draft until reviewed. Never use chat as sole truth.

## 5. Input envelope
For each submitted item, provide applicable fields: title; artifact type; purpose/question; canonical or proposed ID; source URI/original path; creator and date; version/revision/commit/timestamp; territory/domain/layer/type; project and owner; license; extraction method; evidence quality/confidence; related concepts/requirements/decisions/components/tests; review status and next action.

Mark missing optional values unknown or not applicable; never fabricate. Required schema fields must be satisfied.

## 6. Trust and maturity
Do not confuse source existence with correctness, research with verification, implementation with validation, a passing unit test with production readiness, or AI summary with primary evidence. Use canonical status vocabulary and schemas.

## 7. Inspect a concept
Review identity/aliases, definition/scope, taxonomy, purpose/mechanism, architecture/interfaces, inputs/outputs/states/errors, lifecycle/dependencies, typed relations, implementations/version constraints, trade-offs, verification, evidence/provenance and open questions.

## 8. Typed relationships
Relations such as IS-A, PART-OF, DEPENDS-ON, USES, IMPLEMENTS, EXTENDS, CONTROLS, EXECUTES, OBSERVES and COMPETES-WITH are typed claims. Verify direction and source. Uncertain relations should remain proposed or unresolved.

## 9. Documented API
The root README documents:
- GET /api/v1/search?q=...
- GET /api/v1/facets
- GET /api/v1/concepts/{id}
- GET /api/v1/documents/{id}
- GET /api/v1/taxonomy

Use API docs served by the exact running commit for request/response details. Do not assume undocumented write endpoints.

## 10. Issue and correction reports
Include commit SHA, OS, Python version, reproduction steps, expected/actual behavior and sanitized logs. For knowledge corrections, cite primary sources and affected IDs/relations.

## 11. Privacy and stewardship
Do not submit passwords, tokens, private keys, unnecessary personal identifiers, confidential customer data or regulated data without an approved secured workflow. Respect copyright, export controls, standards licensing and repository license status.

## 12. Manual acceptance
Instructions are fully validated only after a clean install has been exercised on declared platforms and command outputs/runtime behavior recorded. This manual is a controlled baseline, not proof every path has been tested.
