# VES MVP Plan and Acceptance Criteria

## Delivery strategy
Maintain a complete target architecture but implement through vertical slices. The first deliverable proves model → card → board → relationship → validation → export/import.

| Phase | Scope | Exit evidence |
|---|---|---|
| 0 Foundation | model contract, repository layout, docs and tests | schema review and unit tests |
| 1 Visual workspace | canvas, navigation, inspector and placement | browser flow evidence |
| 2 Cards and gallery | card views, search and Deck CRUD | unit and UI tests |
| 3 Model and boards | entities, typed relations and board types | model consistency tests |
| 4 Forms and validation | schema-driven forms, rule engine and evidence | deterministic validation tests |
| 5 Integration/export | import/export adapters and documentation | round-trip and loss report |
| 6 Cross-platform | desktop/mobile packaging and hardening | install, offline and device QA |

The earlier 13-week estimate is a rough solo-developer planning assumption, not a delivery commitment; specialist integrations may increase it.

## Acceptance criteria
- AC-01 Create and reopen a project.
- AC-02 Create typed entities with stable IDs.
- AC-03 Render one entity as multiple card views without duplication.
- AC-04 Persist board placement.
- AC-05 Create typed relationships with valid endpoints.
- AC-06 Persist Inspector edits.
- AC-07 Gallery and Deck operate on reusable references.
- AC-08 Validate form data against declared schemas.
- AC-09 Produce stable validation codes/severities.
- AC-10 Export/import preserves IDs, properties, relations and placements.
- AC-11 Core editing works offline.
- AC-12 Responsive behavior passes viewport checks.
- AC-13 Imported resources retain source/license metadata.
- AC-14 Import never silently overwrites an existing project.

PASS requires executable evidence; FAIL is reproducible unmet criteria; NOT RUN means no test executed; BLOCKED identifies an external dependency. Documentation completion is not implementation completion.
