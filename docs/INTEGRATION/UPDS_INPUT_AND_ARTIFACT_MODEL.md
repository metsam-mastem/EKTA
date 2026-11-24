# UPDS Input and Artifact Model
**Document ID:** UPDS-INPUT-0001 | **Status:** PROPOSED CONTRACT

## 1. Purpose
Define a universal, format-neutral intake contract for project information. UPDS must preserve original artifacts, create typed metadata records, track transformations and connect evidence to requirements, decisions, components, tests and releases. It must not claim that a file type is ingestible merely because it can be attached to a conversation.

## 2. Intake pipeline
1. **Receive:** capture source URI, file or structured payload with user authorization.
2. **Identify:** classify artifact family and detect format using content signatures where possible; filename extension is not sufficient.
3. **Preserve:** retain immutable original or a controlled external reference; calculate cryptographic checksum for stored binary objects.
4. **Describe:** create metadata record with stable ID, owner, project, source, date, version, rights and classification.
5. **Extract:** optional parser/OCR/ASR/compiler/CAD metadata extractor; record tool/version/config and extraction limitations.
6. **Normalize:** map extracted fields to typed schemas without overwriting original content.
7. **Validate:** schema, required fields, IDs, references, license, security and malware policy.
8. **Review:** human approval for canonical knowledge, decisions, external claims and risky data.
9. **Link:** connect the artifact to EKTA concepts and UPDS project entities with typed edges.
10. **Publish:** commit canonical metadata/derived text and preserve native binary/external artifact according to storage policy.
11. **Monitor:** record supersession, expiry, source changes and broken references.

Each stage emits an auditable status. Failure at a stage must not silently discard the original.

## 3. Artifact families and handling
| Family | Examples | Required preservation and metadata |
|---|---|---|
| Plain text | notes, requirements, procedures, transcripts | encoding, author, date, source, language, context |
| Structured data | YAML, JSON, CSV, XML, tables | schema/version, units, delimiter, encoding, null rules, source |
| Source code | scripts, modules, patches | language, repository, commit, path, license, build/test info |
| Repository snapshot | Git repository, archive | canonical URL, commit/tag, tree/hash, license, retrieval date |
| Documents | PDF, DOCX, ODT, HTML, standards | title, publisher, revision, pages/sections, rights, extraction tool |
| Image/diagram | photo, schematic, chart, screenshot | original resolution, author, capture date, labels, units, annotations |
| Audio/video | recording, lecture, demo | codec, duration, language, creator, transcript timestamps, rights |
| CAD/EDA/CAE | STEP, STL, native CAD, PCB | application/version, units, coordinate system, dependencies, revision |
| Measurement/test | CSV logs, instrument export, report | procedure, setup, calibration, environment, units, expected/actual |
| Model/dataset | ML weights, dataset, simulation | format, version, provenance, license, schema, checksum, limitations |
| Web source | article, docs, API reference | canonical URL, publisher, retrieval date, version, cited section |
| Conversation/AI output | transcript, generated draft | origin, model/tool, timestamp, prompt context if safe, reviewer, validation status |

## 4. Universal metadata envelope
Required fields should be kept small and stable; family-specific schemas carry the details.

- artifact_id: globally unique, immutable identifier;
- artifact_type: controlled type;
- title: human-readable name;
- project_id: owning project;
- lifecycle_status: draft/proposed/accepted/superseded/archived;
- source: origin URI or local path plus provenance;
- created_at and captured_at: distinguish creation from intake;
- owner: accountable person/team or role;
- revision: source version, commit, document revision or checksum;
- rights: license, access restrictions and redistribution permission;
- classification: sensitivity and retention class;
- integrity: checksum and size for binary artifacts where stored;
- relations: typed references to related entities;
- transformations: derived artifact links and extraction metadata;
- review: reviewer, date, outcome and comments.

The exact field names and enumerations must be reconciled with schemas/upds-document.schema.json before runtime use. This document is a design contract, not an implemented schema.

## 5. Original and derived artifacts
Never overwrite source evidence with OCR, transcription, conversion, redaction or AI summary. Store a directed derivation relation such as DERIVED-FROM and record the method, software/version, configuration, timestamp and operator. Derived text may be indexed; original artifact remains authoritative for its native content.

## 6. Acceptance and rejection
Accept only if identity, provenance, rights and required metadata are sufficient for the intended use. Reject or quarantine when malware is suspected, rights are unclear for redistribution, data is malformed, integrity fails, sensitive data is unauthorized, or source identity cannot be established. A rejected item may remain in a restricted quarantine with reason and retention policy; do not publish it to the knowledge base.

## 7. Input methods
Potential methods: Git commit, local CLI, web form, API, watched folder, repository URL, connector, batch archive and controlled manual entry. Only methods explicitly implemented and documented in a release may be advertised as available. Current EKTA v0.2 is read-only and does not provide a general upload/import UI.

## 8. Security and privacy
Apply least privilege, size limits, file-type allowlists, archive path traversal protection, malware scanning where available, parser sandboxing, secret/PII detection, access controls and retention rules. Never execute uploaded source code as part of ingestion. External fetchers must enforce URL allowlists/SSRF protection and respect robots, terms and copyright. Do not log credentials or raw sensitive payloads.

## 9. Validation and traceability
Validate metadata schema, stable ID uniqueness, project ownership, referenced entity existence, relation type/direction, checksum, rights and review status. Each accepted artifact should be traceable to its source and every derived output should point back to the original. Requirements and decisions should link to implementation and verification evidence where applicable.

## 10. Acceptance criteria for implementation
- A supported artifact can be received without losing original bytes.
- Stable ID and checksum are generated deterministically or collision-safely.
- Schema and rights validation fail closed.
- Derivations retain source and tool provenance.
- Quarantine is separate from published knowledge.
- Typed links resolve or remain explicitly unresolved.
- Tests cover malformed inputs, duplicate IDs, unsafe archives, oversized files, missing rights, secrets and transformation lineage.
- The UI/API only advertises implemented input methods.
