"""Small, dependency-free reader and morphology summaries for SWC files."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, TextIO
import math

@dataclass(frozen=True)
class Node:
    node_id: int
    kind: int
    x: float
    y: float
    z: float
    radius: float
    parent: int

@dataclass(frozen=True)
class Morphology:
    nodes: tuple[Node, ...]
    comments: tuple[str, ...] = ()

    @property
    def by_id(self) -> dict[int, Node]:
        return {n.node_id: n for n in self.nodes}

def parse_swc(source: str | Path | TextIO | Iterable[str]) -> Morphology:
    """Parse SWC rows, rejecting duplicate ids, malformed rows and missing parents.

    Accepts a path, a text stream, or an iterable of lines. A root has parent -1.
    This validates structural references but does not assert that a morphology is
    biologically complete or that it contains exactly one connected tree.
    """
    close = False
    if isinstance(source, (str, Path)):
        stream = open(source, encoding="utf-8", errors="replace")
        close = True
    elif hasattr(source, "read"):
        stream = source
    else:
        stream = source
    nodes: list[Node] = []
    comments: list[str] = []
    seen: set[int] = set()
    try:
        for lineno, raw in enumerate(stream, 1):
            line = raw.strip()
            if not line:
                continue
            if line.startswith("#"):
                comments.append(line[1:].strip())
                continue
            fields = line.split()
            if len(fields) != 7:
                raise ValueError(f"line {lineno}: expected 7 SWC columns, got {len(fields)}")
            try:
                node_id, kind, x, y, z = int(fields[0]), int(fields[1]), *map(float, fields[2:5])
                radius, parent = float(fields[5]), int(fields[6])
            except ValueError as exc:
                raise ValueError(f"line {lineno}: invalid numeric field") from exc
            if node_id < 0 or node_id in seen:
                raise ValueError(f"line {lineno}: node id must be unique and non-negative")
            if not all(math.isfinite(v) for v in (x, y, z, radius)) or radius < 0:
                raise ValueError(f"line {lineno}: coordinates/radius must be finite and radius non-negative")
            seen.add(node_id)
            nodes.append(Node(node_id, kind, x, y, z, radius, parent))
    finally:
        if close:
            stream.close()
    if not nodes:
        raise ValueError("SWC has no nodes")
    ids = {n.node_id for n in nodes}
    missing = [n.node_id for n in nodes if n.parent != -1 and n.parent not in ids]
    if missing:
        raise ValueError(f"nodes reference missing parent(s): {missing[:5]}")
    if not any(n.parent == -1 for n in nodes):
        raise ValueError("SWC has no root (parent -1)")
    return Morphology(tuple(nodes), tuple(comments))

def summarize(morphology: Morphology) -> dict[str, object]:
    """Return deterministic topological and geometric summary (input coordinate units)."""
    nodes = morphology.nodes
    by_id = morphology.by_id
    children = {n.node_id: 0 for n in nodes}
    edge_lengths = []
    for n in nodes:
        if n.parent != -1:
            parent = by_id[n.parent]
            children[n.parent] += 1
            edge_lengths.append(math.dist((n.x,n.y,n.z),(parent.x,parent.y,parent.z)))
    xs, ys, zs = [n.x for n in nodes], [n.y for n in nodes], [n.z for n in nodes]
    kinds: dict[str, int] = {}
    for n in nodes:
        kinds[str(n.kind)] = kinds.get(str(n.kind), 0) + 1
    roots = [n.node_id for n in nodes if n.parent == -1]
    return {
        "node_count": len(nodes), "root_count": len(roots), "roots": roots,
        "branch_point_count": sum(v > 1 for v in children.values()),
        "terminal_count": sum(v == 0 for v in children.values()),
        "edge_count": len(edge_lengths), "total_path_length": sum(edge_lengths),
        "bounding_box": {"x": [min(xs), max(xs)], "y": [min(ys), max(ys)], "z": [min(zs), max(zs)]},
        "node_types": kinds,
    }
