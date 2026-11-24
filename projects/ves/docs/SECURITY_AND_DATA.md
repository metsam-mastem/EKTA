# VES Security and Data Handling

- v0.1 browser prototype sends no project data to a server.
- Browser local storage is not encrypted or a secure vault. Do not store secrets, credentials or regulated personal data.
- Exported JSON is plain text and must be protected according to its classification.
- Future importers must stage data and reject path traversal, symlinks and unbounded archives.
- Future plugins are capability-scoped and denied network/filesystem access by default.
- External assets retain provenance and license metadata.
- Security review/threat modeling is required before network, multi-user or third-party plugin execution is enabled.
