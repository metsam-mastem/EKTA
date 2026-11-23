"""FastAPI entry point for the EKTA local-first knowledge runtime."""
from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .repository import AtlasRepository

DEFAULT_ROOT = Path(os.environ.get("EKTA_ROOT", Path(__file__).resolve().parents[2]))
repository = AtlasRepository(DEFAULT_ROOT)

app = FastAPI(
    title="EKTA Knowledge Runtime",
    version="0.1.0",
    description="Read-only API over EKTA's canonical Git-native knowledge base.",
)


@app.get("/health", tags=["system"])
def health() -> dict:
    return {"status": "ok", "runtime": "ekta", "version": "0.1.0"}


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
    limit: int = Query(default=30, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> dict:
    return repository.search(
        q, domain=domain, layer=layer, knowledge_type=knowledge_type,
        status=status, kind=kind, limit=limit, offset=offset,
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
