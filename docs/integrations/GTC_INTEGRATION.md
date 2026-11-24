# GTC Integration into EKTA

**Status:** INTEGRATED — pinned Git submodule on an integration branch; pending PR review  
**Audit date:** 2026-11-24  
**Canonical upstream:** https://github.com/metsam-mastem/GTC  
**Pinned commit:** `2f0229bd622de4e9ce22196e57fb986659dc7934`  
**Pinned tree:** `2f0229bd622de4e9ce22196e57fb986659dc7934` (GTC main commit/tree root)  
**EKTA integration path:** `integrations/gtc`

## 1. Integration decision

GTC remains an independently governed, independently versioned project. EKTA connects to it through a Git submodule pinned to an exact upstream commit. This provides a reproducible reference to the complete GTC source tree without silently merging project histories, duplicating canonical records, or creating competing sources of truth.

- GTC remains authoritative for its device/component records, source registry, schemas, importer, runtime, explorer, tests, workflows, and project roadmap.
- EKTA remains authoritative for cross-domain taxonomy, concept records, engineering methods, research synthesis, architecture decisions, and portfolio-level navigation.
- This integration does not transfer ownership or relicense GTC content.
- Updating the submodule pointer requires a reviewed change and an updated audit record.

## 2. What was inspected

At the pinned revision, the GTC Git tree contains **94 paths: 68 files and 26 directories**, with approximately **395,654 bytes** of file content.

| Area | Files | Observed content |
|---|---:|---|
| Data records and registries | 23 | 20 device/component dossiers plus manufacturer, source, and taxonomy registries |
| Documentation | 13 | Architecture, identity, data model, ingestion, licensing, source audit, taxonomy, explorer, roadmap |
| Schemas | 6 | Device, component, claim, source, asset, engineering-observation contracts |
| Web explorer | 6 | HTML, JavaScript, CSS, service worker, manifest, favicon |
| Tools | 5 | Python runtime, TechAPI importer/discovery, package markers |
| Tests | 2 | Runtime and TechAPI discovery tests |
| Research | 2 | Mobile history seed and dated import batch |
| Templates | 3 | Device, component, engineering observation |
| GitHub workflows | 4 | Validation, TechAPI inventory, source audit, Pages workflow |
| Root files | 4 | README, MIT code license, data license, gitignore |

The 20 dossier files are distributed as follows: 8 phones, 1 tablet, 3 laptops, 1 single-board computer, 1 CPU, 1 GPU, 4 SoCs, and 1 wearable. These are a starter set, not a coverage-complete catalogue.

## 3. Architecture findings

GTC is data-first and repository-native. Its documented layers are:

1. Experience — Persian responsive web atlas and offline-capable PWA shell.
2. Knowledge — entity registry, taxonomy, identity resolution, relationships.
3. Evidence — source-backed claims, documents/assets metadata, observations.
4. Ingestion and validation — import, normalization, deduplication, provenance, schemas, quality gates.
5. Foundation — identifiers, versioning, licensing, security, governance.

Its core entities include manufacturer/brand, product family/model/variant, hardware revision/board, component, SoC/CPU/GPU/MCU/modem, software/firmware, standard/protocol/interface, source/asset, test/observation, and repair procedure.

Its key engineering rule is claim-level provenance: a displayed specification is not treated as a verified fact unless its claim has a traceable source and a reviewed status. Conflicting claims should be retained rather than silently overwritten.

## 4. Runtime and automation evidence

The latest observed GitHub Actions run at audit time was **GTC Validation #22**, on commit `2f0229bd622de4e9ce22196e57fb986659dc7934`, created 2026-11-23 06:36:50 UTC.

Observed result: **PASS**. The job steps for documentation/catalogue validation, unit tests, catalogue-index build, and artifact upload all reported success. The run produced artifact `gtc-catalogue-index` (20,199 bytes; SHA-256 `7775cae99fdf9eabc4620a9e9ec92f14f0664a3f3a0fe3b12a81537cc55b7a89`).

Historical runs include failures and cancellations. This evidence proves only the reported CI run at that commit; it does not establish full functional correctness, source accuracy, deployment, or product readiness.

The GTC release list was empty at audit time. GitHub Pages is documented as a manual workflow; public deployment was not verified.

## 5. Maturity assessment

**Assessment: foundation / early MVP.**

Implemented at the inspected revision:
- Stable device/component identity model and taxonomy.
- Claim-level provenance and source registry.
- JSON-based starter dossiers and machine-readable schemas.
- Standard-library Python validation and catalogue-index generation.
- Controlled TechAPI importer/discovery adapters.
- Automated GitHub validation and source-health workflows.
- Responsive Persian explorer and offline PWA shell.

Not yet established as complete:
- Broad global device/manufacturer/variant coverage.
- Historical mobile inventory across all generations.
- Board-level BOM, schematic, PCB and component mapping.
- Repair/failure corpus and verified repair workflows.
- Device comparison, timeline/lineage, component-to-device graph.
- SQLite FTS5 runtime query layer and offline export.
- Public release and deployment readiness.

## 6. EKTA taxonomy mapping

This is a multi-axis mapping, not an exclusive classification.

**Relevant operational domains**
- `computer-engineering`
- `electrical-electronic`
- `semiconductor-ic`
- `embedded-firmware`
- `operating-systems-platforms`
- `data-engineering`
- `networking-telecommunications`
- `systems-engineering`
- `testing-verification-validation-quality`
- `documentation-standards-governance`

**Relevant engineering layers**
- `human-experience`
- `application-agent`
- `service-data`
- `platform-runtime`
- `operating-system`
- `firmware-control`
- `hardware-architecture`
- `physical-implementation`

**Knowledge types**
- `architecture`, `component`, `interface`, `process`, `workflow`, `specification`, `tool`, `model`, `research`, `evidence`, `test`, `implementation`, `playbook`.

**EKTA workspaces**
- DISCOVERY: discover upstream hardware datasets, manufacturers, model aliases and source candidates.
- ENCYCLOPEDIA: normalize accepted hardware/device/component concepts and relationships.
- DECISION LAB: assess dataset selection, licensing, schema evolution and technical trade-offs.
- EXECUTION LAB: run import, validation, evidence review, regression tests and release procedures.

## 7. Licensing and reuse boundaries

GTC declares:
- Code and documentation: MIT, see upstream `LICENSE`.
- Original GTC-curated database contributions: CC BY-SA 4.0, subject to the limits in `DATA_LICENSE.md`.
- Third-party datasets and assets: their own licenses and restrictions remain in force.

EKTA's repository license status is currently undecided. Therefore this integration uses a submodule rather than copying or relicensing upstream material. Any later extraction of records or code into EKTA must preserve required notices, attribution, share-alike obligations where applicable, and source-specific restrictions. A public URL does not grant redistribution rights.

## 8. Reproducible checkout

Clone EKTA with the pinned GTC source:

```bash
git clone --recurse-submodules https://github.com/metsam-mastem/EKTA.git
```

For an existing checkout:

```bash
git submodule update --init --recursive
```

Inspect the exact GTC revision:

```bash
git -C integrations/gtc rev-parse HEAD
```

Expected revision: `2f0229bd622de4e9ce22196e57fb986659dc7934`.

## 9. Next work packages

| ID | Work package | Acceptance evidence |
|---|---|---|
| GTC-EKTA-01 | Crosswalk GTC JSON schemas to EKTA concept/source/implementation records | Field mapping, loss report, schema tests |
| GTC-EKTA-02 | Build an EKTA source and implementation record for GTC | Valid canonical record with exact commit and license boundary |
| GTC-EKTA-03 | Add graph export mapping for GTC entity/relation vocabulary | Typed node/edge mapping and dangling-reference tests |
| GTC-EKTA-04 | Add local integration validation for submodule pin and required upstream files | CI gate fails on missing or changed pin |
| GTC-EKTA-05 | Build a curated, claim-level evidence intake path | Human-reviewed sample batch with source and license checks |
| GTC-EKTA-06 | Reassess GTC roadmap and coverage periodically | Dated coverage report with reproducible counts |

## 10. Verification boundary

This integration change records the upstream state inspected and pins the source repository. It does **not** claim that EKTA's runtime has loaded or indexed GTC, that the submodule clone was exercised locally, or that EKTA CI passed on this change. Those checks remain pending until the PR workflow reports results.
