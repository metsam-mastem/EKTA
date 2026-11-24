# EKTA Parallel Development Orchestration

Registry: orchestration/WORKSTREAMS.yml  
Snapshot: 2026-11-24  
Canonical repository: https://github.com/metsam-mastem/EKTA  
Canonical branch: main

## Objective

Coordinate independent EKTA subsystems through parallel research and implementation while preserving one canonical knowledge model, one governed main branch, isolated PRs, and verifiable evidence. The YAML registry is the durable work queue for ownership, dependencies, status, outputs, and acceptance gates.

## Parallel lanes

| Lane | Workstreams | Rule |
|---|---|---|
| Foundations | USDO #13, UMSF #11, MUA #19 | Parallel isolated contracts; coordinate identity, dimensionality, relation semantics, and schema compatibility before cross-integration. |
| Visual engineering | VEL #10, VES #20 | VEL defines visual-model interchange; VES is a separate product environment. Resolve their boundary before claiming integration. |
| Knowledge ingestion | GitHub Docs #8, Concept archive #7 | Source discovery and archive transfer proceed in parallel; no unreviewed source material enters canonical Encyclopedia. |
| Governance and practice | Collaboration Atlas #9, UPDS #23 | Keep content proposed until source, governance, and overlap reviews are complete. |
| Taxonomy views | Engineering Organization Crosswalk #22 | Keep the 14-area map non-canonical; do not replace EKTA taxonomy registries. |

## Repository facts

Ten active product workstreams were inspected on 2026-11-24; PR #3 is closed/unmerged and superseded by clean-mainline PR #23. PR #21 is the separate orchestration PR. GTC is pinned on main at commit 7ea271e00ef2cb010c17bdaa553e1f27645f12ca. Several subsystem branches remain one commit behind main; reconcile before merging. UPDS #23 is 75 commits ahead and 0 behind, replacing the stale PR #3 branch.

| PR | Workstream | Branch | Ahead / behind main | Next gate |
|---:|---|---|---:|---|
| #20 | VES | project/ves-foundation-v0.1 | 16 / 0 | Exact-head CI PASS (run 348); owner review and VES/VEL boundary ADR |
| #19 | MUA | workbench/mua-foundation-0.1.0 | 6 / 1 | Exact-head CI PASS (run 221); reconcile one-commit mainline gap |
| #13 | USDO | knowledge/usdo-ontology-foundation | 5 / 1 | Exact-head CI PASS (run 210); reconcile one-commit mainline gap |
| #11 | UMSF | architecture/umsf-coordinate-framework-v0.1 | 19 / 1 | Exact-head CI PASS (run 288); owner review and branch freshness reconciliation |
| #10 | VEL | project/vel-language-v0.1 | 6 / 1 | Exact-head CI PASS (run 207); reconcile one-commit mainline gap |
| #9 | Collaboration Atlas | feat/collaboration-organizational-atlas | 13 / 1 | Exact-head CI PASS (run 184); reconcile one-commit mainline gap and source review |
| #8 | GitHub Docs | integration/github-docs-source-v1 | 9 / 1 | Exact-head CI PASS (run 183); bounded collector proof and branch refresh |
| #7 | Archive intake | archive-intake/ekta-concepts-2026-11-23 | 3 / 1 | BLOCKED: staged EKTA-CON-000008 conflicts with canonical Hardware Knowledge Atlas ID; resolve immutable ID allocation before transfer |
| #22 | Engineering Organization Crosswalk | knowledge/engineering-organization-v1 | 16 / 0 | Exact-head CI PASS (run 289); owner review of source interpretation and non-canonical scope |
| #23 | UPDS | integration/upds-independent-continuity | 75 / 0 | Exact-head CI PASS (run 408); owner review and clean-clone recovery test |
| #3 | UPDS | integration/upds-documentation-architecture | 57 / 35 | Scope reconciliation; rebase; CI |

## Recent verified execution

- UMSF PR #11 latest inspected head `fcf6ea61f01b23a0d410313fe6c3ef172e9bb4ca` passed Actions run [#288](https://github.com/metsam-mastem/EKTA/actions/runs/45304547566): documentation validation, unit/runtime tests, frontend validation, and graph export. The PR remains draft/unmerged.
- Orchestration PR #21 revision `8dfe76838da79bfff5cb1f1ebae09b897cb5766d` passed Actions run [#382](https://github.com/metsam-mastem/EKTA/actions/runs/45305073885), including the workstream registry validator, integration pin checks, cycle detection, and archive collision regression test. Later registry refreshes are being revalidated in run #418.

- UPDS PR #23 exact head `8453a2d179490969a5b2262c8d8e34ba957d3d5c` passed Actions run [#408](https://github.com/metsam-mastem/EKTA/actions/runs/45305319405); clean-clone recovery and restore remain NOT RUN.\n\n## New integration and integrity finding

- GTC is pinned at `integrations/gtc` to upstream commit `2f0229bd622de4e9ce22196e57fb986659dc7934`. EKTA main includes the integration audit and the canonical Hardware Knowledge Atlas concept record `EKTA-CON-000008`.
- PR #7's staging manifest assigns `EKTA-CON-000008` to Operating System. This is a confirmed stable-ID collision, not a theoretical risk. The archive branch must remain blocked until the source record receives an owner-approved new immutable ID and the manifest/hash/provenance mapping is updated.
- GTC submodule pinning does not mean EKTA runtime ingestion or cross-schema graph mapping is implemented.

## Shared architecture decisions

1. EKTA remains canonical. Subsystems may own versioned contracts but reference EKTA stable IDs; they do not create competing knowledge stores.
2. No taxonomy replacement. Territory, domain, layer, knowledge type, and relation registries retain distinct meanings. New facets are namespaced and reviewed.
3. No semantic overloading. UMSF coordinates are semantic addresses, not Cartesian measurements; MUA coordinate frames are explicit mathematical objects; VEL/VES board placement is UI/model layout. These coordinate systems are not interchangeable.
4. Typed graph relations remain separate from coordinates and topology. Edges are not inferred from visual proximity, coordinate proximity, or shared labels.
5. Validation is layered: syntax, schema, referential integrity, semantic validity, mathematical correctness, and runtime behavior are separate checks.
6. Source material is staged with provenance, version, retrieval date, license, and checksums where applicable. Canonical promotion requires review.
7. No hidden runtime coupling. VES, VEL, MUA, UMSF, and USDO remain optional; EKTA core must not import optional engines without an approved adapter contract.
8. No automatic merges. Every PR retains its review gate; this orchestration does not approve or merge workstreams.

## Dependency graph

EKTA registries -> USDO facets -> MUA object semantics  
EKTA registries -> UMSF semantic coordinates -> MUA coordinate references  
USDO + UMSF -> VEL model semantics -> VES visual studio  
External sources/archive -> provenance + staging -> human review -> canonical Encyclopedia  
Collaboration Atlas -> Execution Lab practices  
UPDS #23 -> proposed cross-cutting document governance
GTC pinned submodule -> hardware knowledge atlas source integration

This is a planned dependency graph, not evidence of completed runtime integration.

## Execution protocol

- Parallelize source research, isolated subsystem code, examples, and tests.
- Serialize edits to shared registries, schemas, README, CI workflow, and canonical main.
- Every PR records exact head SHA, base, changed paths, CI run, test evidence, limitations, and next dependency.
- CI PASS is revision-specific; any later commit requires a new run.
- Keep PRs draft until exact-head acceptance gates and human review complete.
- Do not merge stale, diverged, or unreviewed shared-contract changes.
- Use PASS, FAIL, NOT RUN, and BLOCKED only with evidence.

## Immediate order

1. Refresh all PR branches against current main and run exact-head CI.
2. Review and freeze USDO facet semantics and UMSF coordinate invariants.
3. Revalidate MUA schema/example conformance after branch refresh.
4. Reconcile VEL/VES contracts and decide their boundary in an ADR.
5. Run Collaboration Atlas source and taxonomy checks.
6. Execute the GitHub Docs collector with a bounded limit; preserve a failure ledger.
7. Complete archive transfer with byte-for-byte SHA-256 checks before canonical review.
8. Review clean-mainline UPDS PR #23 after exact-head CI; keep PR #3 closed and unmerged.
9. Review the 14-area Engineering Organization Crosswalk #22 as a non-canonical navigation overlay.
10. Keep archive PR #7 blocked until the EKTA-CON-000008 collision is resolved.

## Session boundary

This registry and the linked GitHub PRs/Actions are the durable work queue. No autonomous background agent is implied; work resumes from GitHub evidence. A new session reads this document, the YAML registry, the relevant PR branch, and its latest CI run before editing.
