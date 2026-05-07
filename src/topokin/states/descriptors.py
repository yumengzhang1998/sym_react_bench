from __future__ import annotations

import networkx as nx
import numpy as np

from topokin.graph.rings import ring_count_by_size
from topokin.types import TopologyDescriptor, TopologyState


def descriptor_from_adjacency(adj: np.ndarray, level: int = 1) -> TopologyDescriptor:
    rings = ring_count_by_size(adj, max_size=6)
    g = nx.from_numpy_array(adj)
    n_edges = g.number_of_edges()
    n_comp = nx.number_connected_components(g)
    mean_degree = int(round(np.mean([d for _, d in g.degree()]) if g.number_of_nodes() else 0))
    if level == 1:
        vals, labels = (rings[3], rings[4], rings[5]), ("n3", "n4", "n5")
    elif level == 2:
        vals, labels = (rings[3], rings[4], rings[5], rings[6]), ("n3", "n4", "n5", "n6")
    else:
        vals = (rings[3], rings[4], rings[5], rings[6], n_edges, n_comp, mean_degree)
        labels = ("n3", "n4", "n5", "n6", "n_edges", "n_components", "mean_degree")
    return TopologyDescriptor(values=tuple(vals), labels=tuple(labels))


def to_topology_state(desc: TopologyDescriptor) -> TopologyState:
    m = dict(zip(desc.labels, desc.values))
    return TopologyState(m.get("n3", 0), m.get("n4", 0), m.get("n5", 0), m.get("n6", 0))
