"""Structural validation primitives for the MUA foundation.

These checks validate record shape and graph references. They do not prove
mathematical truth or perform symbolic/numerical computation.
"""
from __future__ import annotations

import math
import re
from collections.abc import Mapping, Sequence
from typing import Any

_UMO_ID = re.compile(r"^UMO-[A-Z0-9][A-Z0-9._-]{2,95}$")
_REVISION = re.compile(r"^\d+\.\d+\.\d+$")


def validate_mathematical_object(record: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, Mapping):
        return ["record must be a mapping"]
    object_id = record.get("id")
    if not isinstance(object_id, str) or not _UMO_ID.fullmatch(object_id):
        errors.append("id must match UMO-[A-Z0-9][A-Z0-9._-]{2,95}")
    if record.get("schema_version") != "0.1.0":
        errors.append("schema_version must be '0.1.0'")
    kind = record.get("kind")
    if not isinstance(kind, str) or len(kind.strip()) < 2:
        errors.append("kind must be a non-empty string of at least 2 characters")
    revision = record.get("revision")
    if not isinstance(revision, str) or not _REVISION.fullmatch(revision):
        errors.append("revision must use MAJOR.MINOR.PATCH")
    identity = record.get("identity")
    if not isinstance(identity, Mapping) or not isinstance(identity.get("canonical_name"), str) or len(identity["canonical_name"].strip()) < 2:
        errors.append("identity.canonical_name is required")
    semantics = record.get("semantics")
    if not isinstance(semantics, Mapping) or not isinstance(semantics.get("definition"), str) or len(semantics["definition"].strip()) < 8:
        errors.append("semantics.definition must contain at least 8 non-whitespace characters")
    representations = record.get("representations")
    allowed = {"symbolic", "textual", "tabular", "2d", "3d", "spatial", "graph", "procedural", "multimodal"}
    if not isinstance(representations, list) or not representations:
        errors.append("representations must be a non-empty list")
    else:
        for index, item in enumerate(representations):
            if not isinstance(item, Mapping) or item.get("representation_type") not in allowed:
                errors.append(f"representations[{index}].representation_type is invalid or missing")
    relations = record.get("relations", [])
    if not isinstance(relations, list):
        errors.append("relations must be a list")
    else:
        for index, relation in enumerate(relations):
            if not isinstance(relation, Mapping):
                errors.append(f"relations[{index}] must be a mapping")
                continue
            predicate = relation.get("predicate")
            if not isinstance(predicate, str) or not re.fullmatch(r"[A-Z][A-Z0-9_]*", predicate):
                errors.append(f"relations[{index}].predicate must be an uppercase relation key")
            target = relation.get("target_id")
            if not isinstance(target, str) or not target.strip():
                errors.append(f"relations[{index}].target_id is required")
    return errors


def validate_coordinate_frame(frame: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(frame, Mapping):
        return ["frame must be a mapping"]
    dimension = frame.get("dimension")
    if not isinstance(dimension, int) or isinstance(dimension, bool) or dimension < 1:
        return ["dimension must be a positive integer"]
    axes = frame.get("axes")
    if not isinstance(axes, list):
        errors.append("axes must be a list")
    else:
        if len(axes) != dimension:
            errors.append("axes count must equal dimension")
        axis_ids = [axis.get("id") for axis in axes if isinstance(axis, Mapping)]
        if len(axis_ids) != len(axes):
            errors.append("every axis must be a mapping")
        if len(axis_ids) != len(set(axis_ids)):
            errors.append("axis IDs must be unique")
        for index, axis in enumerate(axes):
            if not isinstance(axis, Mapping) or not isinstance(axis.get("id"), str) or not isinstance(axis.get("label"), str):
                errors.append(f"axes[{index}] requires string id and label")
    origin = frame.get("origin")
    if not isinstance(origin, list) or len(origin) != dimension:
        errors.append("origin length must equal dimension")
    elif any(not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value) for value in origin):
        errors.append("origin values must be finite numbers")
    return errors


def validate_relation_graph(records: Sequence[Mapping[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    for index, record in enumerate(records):
        object_id = record.get("id") if isinstance(record, Mapping) else None
        if not isinstance(object_id, str) or not object_id:
            errors.append(f"records[{index}] has no usable id")
        elif object_id in ids:
            errors.append(f"duplicate object id: {object_id}")
        else:
            ids.add(object_id)
    for record in records:
        if not isinstance(record, Mapping):
            continue
        source_id = record.get("id", "<unknown>")
        relations = record.get("relations", [])
        if not isinstance(relations, list):
            continue
        for relation in relations:
            if isinstance(relation, Mapping):
                target_id = relation.get("target_id")
                if isinstance(target_id, str) and target_id not in ids:
                    errors.append(f"{source_id} references missing target {target_id}")
    return errors
