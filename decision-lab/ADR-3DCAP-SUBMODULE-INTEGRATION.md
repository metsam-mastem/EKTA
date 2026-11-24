# ADR — Connect 3DCAP to EKTA through a pinned submodule

**ID:** EKTA-ADR-3DCAP-001 | **Status:** PROPOSED | **Date:** 2026-11-24

## Context
3DCAP is an independent Android-first capture/reconstruction-handoff project. EKTA needs source access for knowledge extraction, but both repositories have separate identities. EKTA's license is undecided; 3DCAP has no declared license at the inspected revision.

## Decision proposal
Connect the complete 3DCAP source tree through a Git submodule at `integrations/3dcap`, pinned to `b72561384a2a5a1b838167e534bb32eac756c9be`. Keep the integration dossier, crosswalk, evidence register, license/dependency review and handoff in `docs/integrations/`.

Do not copy or vendor upstream source, docs or assets into EKTA canonical files. Do not merge 3DCAP history into EKTA.

## Authority
- 3DCAP owns its app, capture pipeline, Passport, export, COLMAP runner, tests, build and roadmap.
- EKTA owns taxonomy, canonical concepts, cross-project relations, research synthesis, decisions and knowledge governance.
- Pin updates require a reviewed EKTA change and do not rewrite upstream 3DCAP.

## Consequences
**Benefits:** complete source is inspectable; exact revision is reproducible; project identity is preserved; license review precedes extraction.

**Costs:** clones must initialize submodules; the pin may lag upstream; EKTA CI must explicitly checkout submodules if it later tests their contents; a source pin does not make 3DCAP buildable or validated.

## Revisit when
3DCAP publishes a license, EKTA selects its own license, code/data extraction is proposed, or upstream ownership/visibility/license/location changes.
