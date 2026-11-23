# Canonical Concept Schema

| Field | Type | Required | Meaning |
|---|---|---:|---|
| id | string | yes | Immutable stable ID |
| canonical_name | string | yes | Preferred label |
| status | enum | yes | Evidence/review state |
| definition | text | yes | Distinguishing definition |
| scope | text | yes | Included/excluded meanings |
| domains | list | yes | Domain IDs |
| layers | list | yes | Layer IDs |
| knowledge_types | list | yes | Type IDs |
| aliases | list | no | Synonyms, acronyms, translations |
| purpose | text | yes | Why it exists |
| role | text | yes | Function within a system |
| architecture | text | no | Structural context |
| components | list | no | Constituent parts |
| mechanism | text | yes | How it works |
| lifecycle | text | no | States and transitions |
| inputs/outputs | lists | no | Input and output contracts |
| interfaces/dependencies | lists | no | Contracts and dependencies |
| relationships | list | no | Typed graph edges |
| patterns/techniques | lists | no | Related practices |
| implementations/standards | lists | no | Inspectable implementations and standards |
| tradeoffs | text | yes | Limitations and compromises |
| verification | list | yes | How claims/behavior are checked |
| sources | list | yes | Provenance references |
| confidence | enum | yes | low, medium, high with rationale |
| created/updated | dates | yes | Record dates |
| revision | string | yes | Record revision |

## ID prefixes
EKTA-CON concept; EKTA-TEC technique; EKTA-ARC architecture; EKTA-CMP component; EKTA-STD standard; EKTA-TOL tool; EKTA-SRC source; EKTA-DEC decision; EKTA-WFL workflow; EKTA-TST test. IDs are never recycled.

## Status
DRAFT, PROPOSED, RESEARCHED, VERIFIED, IMPLEMENTED, VALIDATED, DEPRECATED, BLOCKED, NOT_RUN.

## Relationship object
predicate (controlled relation), target (stable ID), context (optional), source (optional), status (proposed/researched/verified).

Canonical records use Markdown with YAML front matter. A future JSON Schema may formalize machine validation.
