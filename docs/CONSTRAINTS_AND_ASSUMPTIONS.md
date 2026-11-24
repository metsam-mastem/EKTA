# Constraints and Assumptions
**Snapshot:** 2026-11-24

## Hard constraints
- Canonical repository: https://github.com/metsam-mastem/EKTA.
- Git repository and approved project artifacts are the durable source of truth; chat/model memory is supplemental.
- Do not merge independent projects or repositories without explicit authorization.
- Do not merge PRs or promote PROPOSED architecture to APPROVED without owner review.
- Preserve stable IDs, canonical records, repository history and existing behavior.
- Do not change EKTA license status; license remains undecided.
- Do not add Supabase Cloud, hosted databases or other recurring cloud dependencies without an explicit decision.
- Do not silently change taxonomy, schema, runtime interfaces or project scope.
- Use TDD for new behavior and exact commit-bound evidence for verification claims.
- Do not commit credentials, tokens, private keys, secrets or sensitive personal data.
- Do not execute imported code during ingestion.
- Do not claim support for an artifact input unless the current release implements and tests it.

## Project architecture assumptions — proposed until approved
- UPDS is a bounded, cross-cutting subsystem within EKTA and remains separable.
- EKTA owns shared engineering concepts, taxonomy and typed knowledge vocabulary.
- UPDS owns project-specific requirements, plans, decisions, change/risk, evidence, configuration and handoff records.
- Git-native structured files are the initial canonical store; indexes/caches are rebuildable.
- Large binary artifacts should be referenced by immutable URI plus checksum or stored under an explicit artifact policy, not casually committed to Git.

## Product baseline assumptions
- Runtime 0.2 + Workspace 0.4 is the current documented user-facing baseline.
- Workspace import is bounded Markdown/YAML/JSON staging only; it does not write canonical encyclopedia records.
- Search is deterministic lexical search; semantic/AI search is not available.
- Current product documentation describes supported desktop setup; no Android APK or one-click installer is claimed.

## Review triggers
Revisit assumptions when owner approves ADR-0003, a new release changes runtime capabilities, a license is selected, a new artifact storage backend is proposed, or a clean-clone/backup recovery drill exposes gaps.
