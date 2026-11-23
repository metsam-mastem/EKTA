"""Local workspace services: safe staging, drafts, backups, and onboarding diagnostics."""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import uuid
import zipfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

ALLOWED_IMPORTS = {".md", ".markdown", ".yaml", ".yml", ".json"}
BACKUP_ROOTS = (
    "docs", "taxonomy", "encyclopedia", "schemas", "maps", "research",
    "references", "templates", "workflows", "decision-lab", "execution-lab",
    "runtime", "tools", "tests", "scripts", ".github",
)
BACKUP_FILES = (
    "README.md", "PROJECT_CHARTER.md", "CONTRIBUTING.md", "GOVERNANCE.md",
    "CHANGELOG.md", "LICENSE-STATUS.md", "pyproject.toml",
)
MAX_IMPORT_BYTES = 1024 * 1024
MAX_RESTORE_BYTES = 20 * 1024 * 1024
ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9-]{2,63}$")


class WorkspaceError(ValueError):
    """Raised for invalid workspace operations."""


class Workspace:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.state_root = self.root / ".ekta" / "workspace"
        self.import_root = self.state_root / "imports"
        self.draft_root = self.state_root / "drafts"
        self.backup_root = self.state_root / "backups"
        self.restore_root = self.state_root / "restore-staging"

    def _ensure_dirs(self) -> None:
        for path in (self.import_root, self.draft_root, self.backup_root, self.restore_root):
            path.mkdir(parents=True, exist_ok=True)

    def self_test(self) -> dict[str, Any]:
        checks: list[dict[str, str]] = []

        def add(check_id: str, label: str, passed: bool, detail: str) -> None:
            checks.append({"id": check_id, "label": label, "status": "PASS" if passed else "FAIL", "detail": detail})

        add("python", "نسخه Python", sys.version_info >= (3, 11), sys.version.split()[0])
        add("repository", "ریشه مخزن", (self.root / "README.md").is_file(), str(self.root))
        add("taxonomy", "رجیستری طبقه‌بندی", all((self.root / "taxonomy" / name).is_file() for name in ("domains.yml", "territories.yml", "layers.yml")), "domains / territories / layers")
        add("concepts", "دانشنامه مفاهیم", (self.root / "encyclopedia" / "concepts").is_dir(), "encyclopedia/concepts")
        add("docs", "مرکز مستندات", (self.root / "docs").is_dir() and any((self.root / "docs").glob("*.md")), "docs/*.md")
        add("runtime", "ماژول Runtime", (self.root / "runtime" / "ekta_runtime" / "api.py").is_file(), "FastAPI runtime")
        try:
            self._ensure_dirs()
            writable = os.access(self.state_root, os.W_OK)
        except OSError:
            writable = False
        add("workspace-write", "فضای کاری محلی", writable, str(self.state_root))
        failed = sum(item["status"] == "FAIL" for item in checks)
        return {
            "status": "PASS" if failed == 0 else "FAIL",
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "checks": checks,
            "summary": {"total": len(checks), "passed": len(checks) - failed, "failed": failed},
        }

    def documentation_index(self) -> dict[str, Any]:
        directory = self.root / "docs"
        items = []
        for path in sorted(directory.rglob("*.md")):
            if any(part.startswith(".") for part in path.relative_to(directory).parts):
                continue
            relative = path.relative_to(self.root).as_posix()
            first_heading = next((line.lstrip("#").strip() for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("#")), path.stem.replace("-", " ").title())
            items.append({"title": first_heading, "path": relative, "category": path.parent.relative_to(self.root).as_posix()})
        return {"items": items, "count": len(items)}

    def stage_import(self, filename: str, content: str) -> dict[str, Any]:
        suffix = Path(filename).suffix.lower()
        if suffix not in ALLOWED_IMPORTS:
            raise WorkspaceError("فرمت مجاز: Markdown، YAML یا JSON")
        if not filename or Path(filename).name != filename or len(filename) > 180:
            raise WorkspaceError("نام فایل نامعتبر است")
        raw = content.encode("utf-8")
        if len(raw) > MAX_IMPORT_BYTES:
            raise OverflowError("حداکثر اندازه هر ورودی ۱ مگابایت است")
        parsed: Any = None
        validation = "متن دریافت شد؛ هنوز وارد دانشنامه canonical نشده است."
        if suffix in {".yaml", ".yml"}:
            parsed = yaml.safe_load(content)
            if parsed is not None and not isinstance(parsed, (dict, list)):
                raise WorkspaceError("ساختار YAML باید mapping یا list باشد")
            validation = "YAML با safe_load قابل‌خواندن است."
        elif suffix == ".json":
            parsed = json.loads(content)
            if not isinstance(parsed, (dict, list)):
                raise WorkspaceError("ساختار JSON باید object یا array باشد")
            validation = "JSON معتبر است."
        elif content.startswith("---\n"):
            parts = content.split("---", 2)
            if len(parts) != 3:
                raise WorkspaceError("Front matter باید با --- بسته شود")
            metadata = yaml.safe_load(parts[1]) or {}
            if not isinstance(metadata, dict):
                raise WorkspaceError("Front matter باید YAML mapping باشد")
            parsed = {"metadata": metadata, "body": parts[2].lstrip("\n")}
            validation = "Front matter قابل‌خواندن است؛ Schema مفهومی هنوز بررسی نشده است."
        self._ensure_dirs()
        token = uuid.uuid4().hex
        target = self.import_root / f"{token}{suffix}"
        target.write_bytes(raw)
        return {"id": token, "filename": filename, "size": len(raw), "status": "staged", "validation": validation, "stored_as": target.relative_to(self.root).as_posix()}

    def save_draft(self, payload: dict[str, Any]) -> dict[str, Any]:
        record_id = str(payload.get("id", "")).strip()
        name = str(payload.get("canonical_name", "")).strip()
        body = str(payload.get("body", "")).strip()
        if not ID_PATTERN.fullmatch(record_id):
            raise WorkspaceError("شناسه باید از حروف بزرگ، عدد و خط تیره تشکیل شود")
        if not name or len(name) > 180:
            raise WorkspaceError("نام canonical الزامی است و حداکثر ۱۸۰ نویسه دارد")
        if not body or len(body.encode("utf-8")) > MAX_IMPORT_BYTES:
            raise WorkspaceError("بدنه پیش‌نویس خالی یا بزرگ‌تر از ۱ مگابایت است")
        self._ensure_dirs()
        metadata = {
            "id": record_id, "canonical_name": name, "status": "PROPOSED",
            "revision": "0.1.0-draft", "domains": payload.get("domains", []),
            "layers": payload.get("layers", []), "knowledge_types": payload.get("knowledge_types", ["CONCEPT"]),
            "aliases": payload.get("aliases", []),
        }
        rendered = "---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False) + "---\n\n" + body + "\n"
        target = self.draft_root / f"{record_id}.md"
        target.write_text(rendered, encoding="utf-8")
        return {"id": record_id, "status": "draft", "path": target.relative_to(self.root).as_posix(), "canonical_source_changed": False}

    def create_backup(self) -> dict[str, Any]:
        self._ensure_dirs()
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        target = self.backup_root / f"ekta-backup-{timestamp}.zip"
        included = []
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for relative in BACKUP_FILES:
                path = self.root / relative
                if path.is_file():
                    archive.write(path, arcname=f"EKTA/{relative}")
                    included.append(relative)
            for folder in BACKUP_ROOTS:
                base = self.root / folder
                if not base.is_dir():
                    continue
                for path in sorted(base.rglob("*")):
                    if path.is_file() and not path.is_symlink() and not any(part in {".git", ".venv", "__pycache__", "node_modules"} for part in path.parts):
                        relative = path.relative_to(self.root).as_posix()
                        archive.write(path, arcname=f"EKTA/{relative}")
                        included.append(relative)
        return {"filename": target.name, "path": target.relative_to(self.root).as_posix(), "size": target.stat().st_size, "file_count": len(included), "files": included}

    def stage_restore(self, filename: str, archive_base64: str) -> dict[str, Any]:
        if Path(filename).name != filename or not filename.lower().endswith(".zip"):
            raise WorkspaceError("فقط فایل ZIP با نام معتبر پذیرفته می‌شود")
        try:
            raw = base64.b64decode(archive_base64, validate=True)
        except Exception as exc:
            raise WorkspaceError("داده Base64 معتبر نیست") from exc
        if len(raw) > MAX_RESTORE_BYTES:
            raise OverflowError("حداکثر اندازه بسته بازیابی ۲۰ مگابایت است")
        self._ensure_dirs()
        try:
            with zipfile.ZipFile(BytesIO(raw)) as archive:
                entries = archive.infolist()
                if not entries or len(entries) > 5000:
                    raise WorkspaceError("تعداد فایل‌های بسته نامعتبر است")
                for entry in entries:
                    member = PurePosixPath(entry.filename)
                    mode = (entry.external_attr >> 16) & 0o170000
                    if member.is_absolute() or ".." in member.parts or mode == 0o120000:
                        raise WorkspaceError("مسیر ناامن یا symlink در بسته وجود دارد")
                    if not member.parts or member.parts[0] not in {"EKTA", "ekta"}:
                        raise WorkspaceError("ساختار بسته باید در پوشه EKTA قرار گیرد")
                token = uuid.uuid4().hex
                target = self.restore_root / f"{token}.zip"
                target.write_bytes(raw)
                return {"id": token, "filename": filename, "status": "staged", "file_count": len(entries), "size": len(raw), "stored_as": target.relative_to(self.root).as_posix(), "canonical_source_changed": False}
        except zipfile.BadZipFile as exc:
            raise WorkspaceError("فایل ZIP خراب یا نامعتبر است") from exc
