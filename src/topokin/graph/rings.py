from __future__ import annotations

import networkx as nx
import numpy as np


def chordless_cycles(adj: np.ndarray, max_size: int = 6) -> list[list[int]]:
    g = nx.from_numpy_array(adj)
    cycles = nx.cycle_basis(g)
    out: list[list[int]] = []
    for c in cycles:
        if 3 <= len(c) <= max_size:
            sub = g.subgraph(c)
            if sub.number_of_edges() == len(c):
                out.append(sorted(c))
    unique = []
    seen = set()
    for c in out:
        t = tuple(c)
        if t not in seen:
            seen.add(t)
            unique.append(c)
    return unique


def ring_count_by_size(adj: np.ndarray, max_size: int = 6) -> dict[int, int]:
    counts = {k: 0 for k in range(3, max_size + 1)}
    for cyc in chordless_cycles(adj, max_size=max_size):
        counts[len(cyc)] += 1
    return counts
