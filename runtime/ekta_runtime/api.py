"""FastAPI entry point for the EKTA local-first knowledge runtime."""
from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .repository import AtlasRepository
from .workspace import Workspace, WorkspaceError

DEFAULT_ROOT = Path(os.environ.get("EKTA_ROOT", Path(__file__).resolve().parents[2]))
repository = AtlasRepository(DEFAULT_ROOT)
workspace = Workspace(DEFAULT_ROOT)

app = FastAPI(
    title="EKTA Knowledge Runtime",
    version="0.2.0",
    description="Local-first EKTA workbench with safe staged workspace operations.",
)


@app.get("/health", tags=["system"])
def health() -> dict:
    return {"status": "ok", "runtime": "ekta", "version": "0.2.0"}


@app.get("/api/v1/overview", tags=["atlas"])
def overview() -> dict:
    return repository.overview()


@app.get("/api/v1/search", tags=["search"])
def search(
    q: str = Query(default="", max_length=500),
    domain: str | None = None,
    layer: str | None = None,
    knowledge_type: str | None = None,
    status: str | None = None,
    kind: str | None = None,
    territory: str | None = None,
    limit: int = Query(default=30, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> dict:
    return repository.search(
        q, domain=domain, layer=layer, knowledge_type=knowledge_type,
        status=status, kind=kind, territory=territory, limit=limit, offset=offset,
    )


@app.get("/api/v1/facets", tags=["search"])
def facets() -> dict:
    return repository.facets()


@app.get("/api/v1/documents/{document_id}", tags=["documents"])
def document(document_id: str) -> dict:
    item = repository.get_document(document_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return item


@app.get("/api/v1/concepts", tags=["concepts"])
def concepts(
    q: str | None = Query(default=None, max_length=200),
    domain: str | None = None,
    layer: str | None = None,
    status: str | None = None,
) -> dict:
    items = repository.list_concepts(q, domain, layer, status)
    return {"items": items, "count": len(items)}


@app.get("/api/v1/concepts/{concept_id}", tags=["concepts"])
def concept(concept_id: str) -> dict:
    item = repository.get_concept(concept_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Concept not found")
    return item


@app.get("/api/v1/taxonomy", tags=["taxonomy"])
def taxonomy() -> dict:
    return repository.taxonomy()


@app.get("/api/v1/graph", tags=["graph"])
def graph(
    resolved_only: bool = False,
    predicate: str | None = None,
) -> dict:
    data = repository.graph_data
    edges = data["edges"]
    if resolved_only:
        edges = [edge for edge in edges if edge["status"] == "resolved"]
    if predicate:
        edges = [edge for edge in edges if edge["predicate"] == predicate]
    return {**data, "edges": edges, "returned_edge_count": len(edges)}


WEB_ROOT = DEFAULT_ROOT / "runtime" / "web"
if WEB_ROOT.exists():
    app.mount("/assets", StaticFiles(directory=WEB_ROOT), name="assets")

    @app.get("/", include_in_schema=False)
    def home():
        return FileResponse(WEB_ROOT / "index.html")


@app.get("/api/v1/workspace/self-test", tags=["workspace"])
def workspace_self_test() -> dict:
    return workspace.self_test()


@app.get("/api/v1/workspace/docs", tags=["workspace"])
def workspace_docs() -> dict:
    return workspace.documentation_index()


@app.get("/api/v1/workspace/docs/{document_path:path}", tags=["workspace"])
def workspace_doc_content(document_path: str) -> dict:
    target = (DEFAULT_ROOT / document_path).resolve()
    docs_root = (DEFAULT_ROOT / "docs").resolve()
    if docs_root not in target.parents or target.suffix.lower() != ".md" or not target.is_file():
        raise HTTPException(status_code=404, detail="Documentation file not found")
    return {"path": target.relative_to(DEFAULT_ROOT).as_posix(), "content": target.read_text(encoding="utf-8")}


@app.post("/api/v1/workspace/import/preview", tags=["workspace"])
def workspace_import_preview(payload: dict) -> dict:
    try:
        return workspace.stage_import(str(payload.get("filename", "")), str(payload.get("content", "")))
    except OverflowError as exc:
        raise HTTPException(status_code=413, detail=str(exc)) from exc
    except (WorkspaceError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/v1/workspace/drafts", status_code=201, tags=["workspace"])
def workspace_save_draft(payload: dict) -> dict:
    if str(payload.get("id", "")).strip() in repository.by_id:
        raise HTTPException(status_code=409, detail="این شناسه از قبل در دانشنامه canonical وجود دارد")
    try:
        return workspace.save_draft(payload)
    except WorkspaceError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/v1/workspace/backup", tags=["workspace"])
def workspace_backup() -> dict:
    return workspace.create_backup()


@app.post("/api/v1/workspace/restore/preview", tags=["workspace"])
def workspace_restore_preview(payload: dict) -> dict:
    try:
        return workspace.stage_restore(str(payload.get("filename", "")), str(payload.get("archive_base64", "")))
    except OverflowError as exc:
        raise HTTPException(status_code=413, detail=str(exc)) from exc
    except WorkspaceError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


WORKSPACE_PAGE = WEB_ROOT / "workspace.html"
if WORKSPACE_PAGE.exists():
    @app.get("/workspace", include_in_schema=False)
    def workspace_home():
        return FileResponse(WORKSPACE_PAGE)

@app.get("/api/v1/workspace/backups/{filename}", tags=["workspace"])
def workspace_download_backup(filename: str):
    target = (workspace.backup_root / filename).resolve()
    if target.parent != workspace.backup_root.resolve() or target.suffix != ".zip" or not target.is_file():
        raise HTTPException(status_code=404, detail="Backup not found")
    return FileResponse(target, filename=target.name, media_type="application/zip")
