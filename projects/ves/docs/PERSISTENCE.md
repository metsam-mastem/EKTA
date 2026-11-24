# VES Local Persistence Contract

## v0.1 SQLite store
The VES Python core now includes a standard-library SQLite persistence adapter. It stores the versioned project JSON payload and indexed metadata in a single local database.

## Operations
- save(project, expected_updated_at=None): insert or update a project in a transaction.
- load(project_id): reconstruct a Project or return None.
- list_projects(): return metadata only, never the full model payload.
- expected_updated_at: optional optimistic concurrency token. A stale or missing revision raises ConcurrentWriteError.

## Guarantees and limits
- SQLite WAL mode is enabled.
- Writes use BEGIN IMMEDIATE to serialize competing writers.
- A failed save rolls back.
- The model is serialized through Project.to_dict and restored through Project.from_dict.
- This adapter is local single-user persistence; it is not a multi-user sync protocol.
- Backup/restore, schema migration tooling and encrypted storage are not implemented by this slice.

## Tests
The storage test suite covers save/load round-trip, stale revision rejection and metadata-only listing. Run from projects/ves with PYTHONPATH=src python -m unittest discover -s tests -v.
