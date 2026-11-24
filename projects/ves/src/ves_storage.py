"""SQLite-backed local persistence for VES projects (standard library only)."""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from ves_core import Project


class ConcurrentWriteError(RuntimeError):
    """Raised when an optimistic revision check detects a stale writer."""


class SQLiteProjectStore:
    def __init__(self, database_path: str | Path):
        self.database_path = Path(database_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self):
        connection = sqlite3.connect(self.database_path, timeout=5)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self):
        with self._connect() as connection:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute(
                """CREATE TABLE IF NOT EXISTS ves_projects (
                    project_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    schema_version TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )"""
            )

    def save(self, project: Project, expected_updated_at: str | None = None) -> str:
        payload = json.dumps(project.to_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        updated_at = datetime.now(timezone.utc).isoformat()
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            current = connection.execute(
                "SELECT updated_at FROM ves_projects WHERE project_id = ?", (project.id,)
            ).fetchone()
            if expected_updated_at is not None:
                if current is None or current["updated_at"] != expected_updated_at:
                    raise ConcurrentWriteError("project revision changed; reload before saving")
            if current is None:
                connection.execute(
                    "INSERT INTO ves_projects(project_id, name, schema_version, payload_json, updated_at) VALUES (?, ?, ?, ?, ?)",
                    (project.id, project.name, project.schema_version, payload, updated_at),
                )
            else:
                connection.execute(
                    "UPDATE ves_projects SET name = ?, schema_version = ?, payload_json = ?, updated_at = ? WHERE project_id = ?",
                    (project.name, project.schema_version, payload, updated_at, project.id),
                )
            connection.commit()
            return updated_at
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def load(self, project_id: str) -> Project | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT payload_json FROM ves_projects WHERE project_id = ?", (project_id,)
            ).fetchone()
        if row is None:
            return None
        return Project.from_dict(json.loads(row["payload_json"]))

    def list_projects(self) -> list[dict[str, Any]]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT project_id, name, schema_version, updated_at FROM ves_projects ORDER BY updated_at DESC"
            ).fetchall()
        return [
            {"id": row["project_id"], "name": row["name"],
             "schema_version": row["schema_version"], "updated_at": row["updated_at"]}
            for row in rows
        ]
