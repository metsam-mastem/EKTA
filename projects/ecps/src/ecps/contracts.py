"""Federated model-to-view contracts for ECPS 0.1.

ECPS coordinates existing EKTA workstreams; it deliberately does not reimplement
UMSF semantic addresses, MUA mathematical frames, VEL visual grammar, or VES boards.
"""
from __future__ import annotations

from typing import Any

VIEW_COORDINATE_KIND = {
    "semantic-architecture": "semantic-address",
    "geometry-3d": "geometric-frame",
    "workbench-board": "board-layout",
    "visual-diagram": "diagram-topology",
    "dependency-matrix": "relationship-graph",
    "timeline": "temporal-validity",
    "mathematical-plot": "mathematical-representation",
}


def _finding(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path, "message": message, "severity": "ERROR"}


def validate_manifest(manifest: dict[str, Any]) -> list[dict[str, str]]:
    """Validate projection references and prevent coordinate-space conflation."""
    findings: list[dict[str, str]] = []
    if not isinstance(manifest, dict):
        return [_finding("MANIFEST_TYPE", "$", "Manifest must be an object.")]

    source_models = manifest.get("sourceModels")
    spaces = manifest.get("coordinateSpaces")
    projections = manifest.get("projections")
    for key, value in (("sourceModels", source_models), ("coordinateSpaces", spaces), ("projections", projections)):
        if not isinstance(value, list):
            findings.append(_finding(f"{key.upper()}_TYPE", f"$.{key}", f"{key} must be an array."))
    if findings:
        return findings

    sources_by_id: dict[str, dict[str, Any]] = {}
    for index, source in enumerate(source_models):
        path = f"$.sourceModels[{index}]"
        if not isinstance(source, dict):
            findings.append(_finding("SOURCE_MODEL_TYPE", path, "Source model must be an object."))
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id:
            findings.append(_finding("SOURCE_MODEL_ID", f"{path}.id", "Source model id is required."))
            continue
        if source_id in sources_by_id:
            findings.append(_finding("DUPLICATE_SOURCE_MODEL_ID", f"{path}.id", f"Duplicate source model id: {source_id}"))
        else:
            sources_by_id[source_id] = source

    spaces_by_id: dict[str, dict[str, Any]] = {}
    for index, space in enumerate(spaces):
        path = f"$.coordinateSpaces[{index}]"
        if not isinstance(space, dict):
            findings.append(_finding("COORDINATE_SPACE_TYPE", path, "Coordinate space must be an object."))
            continue
        space_id = space.get("id")
        if not isinstance(space_id, str) or not space_id:
            findings.append(_finding("COORDINATE_SPACE_ID", f"{path}.id", "Coordinate space id is required."))
            continue
        if space_id in spaces_by_id:
            findings.append(_finding("DUPLICATE_COORDINATE_SPACE_ID", f"{path}.id", f"Duplicate coordinate space id: {space_id}"))
        else:
            spaces_by_id[space_id] = space
        if space.get("authority") not in {"UMSF", "VEL", "MUA", "VES"}:
            findings.append(_finding("UNKNOWN_COORDINATE_AUTHORITY", f"{path}.authority", "Coordinate-space authority must be a registered workstream."))

    projection_ids: set[str] = set()
    for index, projection in enumerate(projections):
        path = f"$.projections[{index}]"
        if not isinstance(projection, dict):
            findings.append(_finding("PROJECTION_TYPE", path, "Projection must be an object."))
            continue
        projection_id = projection.get("id")
        if not isinstance(projection_id, str) or not projection_id:
            findings.append(_finding("PROJECTION_ID", f"{path}.id", "Projection id is required."))
        elif projection_id in projection_ids:
            findings.append(_finding("DUPLICATE_PROJECTION_ID", f"{path}.id", f"Duplicate projection id: {projection_id}"))
        else:
            projection_ids.add(projection_id)

        view_type = projection.get("viewType")
        expected_kind = VIEW_COORDINATE_KIND.get(view_type)
        if expected_kind is None:
            findings.append(_finding("UNKNOWN_VIEW_TYPE", f"{path}.viewType", f"Unsupported view type: {view_type}"))

        source_id = projection.get("sourceModelRef")
        source = sources_by_id.get(source_id) if isinstance(source_id, str) else None
        if source is None:
            findings.append(_finding("UNKNOWN_SOURCE_MODEL", f"{path}.sourceModelRef", f"Unknown source model: {source_id}"))

        space_id = projection.get("coordinateSpaceRef")
        space = spaces_by_id.get(space_id) if isinstance(space_id, str) else None
        if space is None:
            findings.append(_finding("UNKNOWN_COORDINATE_SPACE", f"{path}.coordinateSpaceRef", f"Unknown coordinate space: {space_id}"))
        elif expected_kind is not None and space.get("kind") != expected_kind:
            findings.append(_finding(
                "COORDINATE_KIND_MISMATCH", f"{path}.coordinateSpaceRef",
                f"View '{view_type}' requires '{expected_kind}', not '{space.get('kind')}'."
            ))

        if source is not None and space is not None and source.get("system") != space.get("authority"):
            findings.append(_finding(
                "AUTHORITY_SOURCE_MISMATCH", f"{path}.coordinateSpaceRef",
                f"Coordinate-space authority '{space.get('authority')}' does not match source system '{source.get('system')}'."
            ))
        if projection.get("mutationPolicy") not in {"read-only", "view-state-only", "explicit-model-edit"}:
            findings.append(_finding("MUTATION_POLICY", f"{path}.mutationPolicy", "Unknown mutation policy."))
    return findings


def compile_projection_plan(manifest: dict[str, Any], projection_id: str) -> dict[str, Any]:
    """Compile a deterministic, renderer-neutral plan; never edits source models."""
    findings = validate_manifest(manifest)
    if findings:
        raise ValueError("Invalid ECPS manifest: " + "; ".join(item["code"] for item in findings))
    projection = next((item for item in manifest["projections"] if item["id"] == projection_id), None)
    if projection is None:
        raise KeyError(projection_id)
    source = next(item for item in manifest["sourceModels"] if item["id"] == projection["sourceModelRef"])
    space = next(item for item in manifest["coordinateSpaces"] if item["id"] == projection["coordinateSpaceRef"])
    return {
        "manifestId": manifest["manifestId"],
        "projectionId": projection["id"],
        "viewType": projection["viewType"],
        "sourceModel": {"id": source["id"], "system": source["system"], "repositoryPath": source["repositoryPath"], "sourceCommit": source["sourceCommit"]},
        "coordinateSpace": {"id": space["id"], "kind": space["kind"], "authority": space["authority"]},
        "coordinateKind": space["kind"],
        "mutationPolicy": projection["mutationPolicy"],
        "readOnly": projection["mutationPolicy"] == "read-only",
        "rendererNeutral": True,
    }
