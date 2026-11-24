"""VEL v0.1 model loading, semantic validation, and DOT export.

This module treats VEL documents as data. It performs no network access,
dynamic imports, expression evaluation, or file writes.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

STATUSES = {
    "DRAFT", "PROPOSED", "APPROVED", "IMPLEMENTED",
    "VERIFIED", "BLOCKED", "DEPRECATED",
}
DIRECTIONS = {"IN", "OUT", "INOUT"}
DEFAULT_CHANNELS = {
    "DATA", "CONTROL", "EVENT", "POWER", "SIGNAL", "MECHANICAL",
    "NETWORK", "DEPENDENCY", "MATERIAL", "FLUID", "THERMAL",
}


def load_model(source: str | Path) -> dict[str, Any]:
    """Load a JSON model from a path or JSON text."""
    if isinstance(source, Path):
        raw = source.read_text(encoding="utf-8")
    else:
        candidate = str(source)
        if candidate.lstrip().startswith(("{", "[")):
            raw = candidate
        else:
            raw = Path(candidate).read_text(encoding="utf-8")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("A VEL model must be a JSON object.")
    return value


def _issue(code: str, path: str, message: str, severity: str = "ERROR") -> dict[str, str]:
    return {"code": code, "path": path, "message": message, "severity": severity}


def validate_model(model: dict[str, Any]) -> list[dict[str, str]]:
    """Return deterministic semantic findings; an empty list means no findings."""
    findings: list[dict[str, str]] = []
    if not isinstance(model, dict):
        return [_issue("MODEL_TYPE", "$", "Model must be an object.")]

    nodes = model.get("nodes", [])
    connections = model.get("connections", [])
    groups = model.get("groups", [])
    if not isinstance(nodes, list):
        return [_issue("NODES_TYPE", "$.nodes", "nodes must be an array.")]
    if not isinstance(connections, list):
        return [_issue("CONNECTIONS_TYPE", "$.connections", "connections must be an array.")]
    if not isinstance(groups, list):
        return [_issue("GROUPS_TYPE", "$.groups", "groups must be an array.")]

    node_by_id: dict[str, dict[str, Any]] = {}
    for index, node in enumerate(nodes):
        path = f"$.nodes[{index}]"
        if not isinstance(node, dict):
            findings.append(_issue("NODE_TYPE", path, "Node must be an object."))
            continue
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id:
            findings.append(_issue("NODE_ID", f"{path}.id", "Node id must be a non-empty string."))
            continue
        if node_id in node_by_id:
            findings.append(_issue("DUPLICATE_NODE_ID", f"{path}.id", f"Duplicate node id: {node_id}."))
        else:
            node_by_id[node_id] = node
        if node.get("status") not in STATUSES:
            findings.append(_issue("NODE_STATUS", f"{path}.status", "Unknown node status."))
        ports = node.get("ports", [])
        if not isinstance(ports, list):
            findings.append(_issue("PORTS_TYPE", f"{path}.ports", "ports must be an array."))
            continue
        seen_ports: set[str] = set()
        for port_index, port in enumerate(ports):
            port_path = f"{path}.ports[{port_index}]"
            if not isinstance(port, dict):
                findings.append(_issue("PORT_TYPE", port_path, "Port must be an object."))
                continue
            port_id = port.get("id")
            if not isinstance(port_id, str) or not port_id:
                findings.append(_issue("PORT_ID", f"{port_path}.id", "Port id must be a non-empty string."))
                continue
            if port_id in seen_ports:
                findings.append(_issue("DUPLICATE_PORT_ID", f"{port_path}.id", f"Duplicate port id {port_id} in node {node_id}."))
            seen_ports.add(port_id)
            if port.get("direction") not in DIRECTIONS:
                findings.append(_issue("PORT_DIRECTION", f"{port_path}.direction", "Direction must be IN, OUT, or INOUT."))
            channels = port.get("channels")
            if not isinstance(channels, list) or not channels or any(not isinstance(item, str) or not item for item in channels):
                findings.append(_issue("PORT_CHANNELS", f"{port_path}.channels", "channels must be a non-empty array of strings."))

    connection_ids: set[str] = set()
    for index, connection in enumerate(connections):
        path = f"$.connections[{index}]"
        if not isinstance(connection, dict):
            findings.append(_issue("CONNECTION_TYPE", path, "Connection must be an object."))
            continue
        connection_id = connection.get("id")
        if not isinstance(connection_id, str) or not connection_id:
            findings.append(_issue("CONNECTION_ID", f"{path}.id", "Connection id must be a non-empty string."))
        elif connection_id in connection_ids:
            findings.append(_issue("DUPLICATE_CONNECTION_ID", f"{path}.id", f"Duplicate connection id: {connection_id}."))
        else:
            connection_ids.add(connection_id)
        if connection.get("status") not in STATUSES:
            findings.append(_issue("CONNECTION_STATUS", f"{path}.status", "Unknown connection status."))
        kind = connection.get("kind")
        if not isinstance(kind, str) or not kind:
            findings.append(_issue("CONNECTION_KIND", f"{path}.kind", "Connection kind must be a non-empty string."))
            continue
        if kind not in DEFAULT_CHANNELS and not re.match(r"^[a-z][a-z0-9-]*:[A-Z][A-Z0-9_]*$", kind):
            findings.append(_issue("UNKNOWN_CHANNEL", f"{path}.kind", f"Channel '{kind}' is not in the core vocabulary or a namespaced extension."))

        resolved_ports: list[tuple[str, dict[str, Any]] | None] = []
        for endpoint_name in ("source", "target"):
            endpoint = connection.get(endpoint_name)
            endpoint_path = f"{path}.{endpoint_name}"
            if not isinstance(endpoint, dict):
                findings.append(_issue("ENDPOINT_TYPE", endpoint_path, "Endpoint must be an object."))
                resolved_ports.append(None)
                continue
            node_id, port_id = endpoint.get("node_id"), endpoint.get("port_id")
            node = node_by_id.get(node_id) if isinstance(node_id, str) else None
            if node is None:
                findings.append(_issue("UNKNOWN_NODE", f"{endpoint_path}.node_id", f"Unknown node '{node_id}'."))
                resolved_ports.append(None)
                continue
            port = next((item for item in node.get("ports", []) if isinstance(item, dict) and item.get("id") == port_id), None)
            if port is None:
                findings.append(_issue("UNKNOWN_PORT", f"{endpoint_path}.port_id", f"Unknown port '{port_id}' on node '{node_id}'."))
                resolved_ports.append(None)
                continue
            resolved_ports.append((endpoint_name, port))

        if resolved_ports[0] is not None:
            direction = resolved_ports[0][1].get("direction")
            if direction not in {"OUT", "INOUT"}:
                findings.append(_issue("SOURCE_DIRECTION", f"{path}.source", "Source port must be OUT or INOUT."))
        if resolved_ports[1] is not None:
            direction = resolved_ports[1][1].get("direction")
            if direction not in {"IN", "INOUT"}:
                findings.append(_issue("TARGET_DIRECTION", f"{path}.target", "Target port must be IN or INOUT."))
        for endpoint_name, resolved in zip(("source", "target"), resolved_ports):
            if resolved is not None:
                accepted_channels = resolved[1].get("channels", [])
                if not isinstance(accepted_channels, list) or kind not in accepted_channels:
                    findings.append(_issue("CHANNEL_MISMATCH", f"{path}.{endpoint_name}.port_id", f"Port does not accept channel '{kind}'."))

    group_ids: set[str] = set()
    for index, group in enumerate(groups):
        path = f"$.groups[{index}]"
        if not isinstance(group, dict):
            findings.append(_issue("GROUP_TYPE", path, "Group must be an object."))
            continue
        group_id = group.get("id")
        if not isinstance(group_id, str) or not group_id:
            findings.append(_issue("GROUP_ID", f"{path}.id", "Group id must be a non-empty string."))
        elif group_id in group_ids:
            findings.append(_issue("DUPLICATE_GROUP_ID", f"{path}.id", f"Duplicate group id: {group_id}."))
        else:
            group_ids.add(group_id)
        members = group.get("node_ids", [])
        if not isinstance(members, list):
            findings.append(_issue("GROUP_MEMBERS", f"{path}.node_ids", "node_ids must be an array."))
            continue
        for member_index, member in enumerate(members):
            if member not in node_by_id:
                findings.append(_issue("UNKNOWN_GROUP_MEMBER", f"{path}.node_ids[{member_index}]", f"Unknown node '{member}'."))

    return findings


def to_dot(model: dict[str, Any]) -> str:
    """Export the graph to Graphviz DOT. This is a view, not a canonical model."""
    def quote(value: Any) -> str:
        return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'

    lines = ["digraph VEL {", "  rankdir=LR;", "  graph [label=" + quote(model.get("name", "VEL model")) + ", labelloc=t];"]
    for node in model.get("nodes", []):
        if not isinstance(node, dict) or not isinstance(node.get("id"), str):
            continue
        label = f"{node.get('label', node['id'])}\\n[{node.get('kind', 'node')}]"
        lines.append(f"  {quote(node['id'])} [label={quote(label)}];")
    for connection in model.get("connections", []):
        if not isinstance(connection, dict):
            continue
        source = connection.get("source", {})
        target = connection.get("target", {})
        if isinstance(source, dict) and isinstance(target, dict):
            source_id, target_id = source.get("node_id"), target.get("node_id")
            if isinstance(source_id, str) and isinstance(target_id, str):
                label = f"{connection.get('kind', 'LINK')} / {connection.get('label', '')}".strip(" /")
                connection_id = connection.get("id", "")
                lines.append(f"  {quote(source_id)} -> {quote(target_id)} [id={quote(connection_id)}, label={quote(label)}];")
    lines.append("}")
    return "\n".join(lines) + "\n"


def canonical_json(model: dict[str, Any]) -> str:
    """Serialize deterministically for stable diffs and content hashing."""
    return json.dumps(model, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
