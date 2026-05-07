from __future__ import annotations

import numpy as np
from ase import Atoms


def _to_dense_symmetric(adj: np.ndarray) -> np.ndarray:
    a = np.array(adj, dtype=int)
    np.fill_diagonal(a, 0)
    return np.maximum(a, a.T)


def build_adjacency_fixed_cutoff(atoms: Atoms, cutoff: float) -> np.ndarray:
    d = atoms.get_all_distances(mic=False)
    adj = ((d > 0.0) & (d <= cutoff)).astype(int)
    return _to_dense_symmetric(adj)


def build_adjacency_element_scaled(atoms: Atoms, base_cutoff: float, scale: dict[str, float]) -> np.ndarray:
    symbols = atoms.get_chemical_symbols()
    n = len(symbols)
    d = atoms.get_all_distances(mic=False)
    adj = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1, n):
            s = (scale.get(symbols[i], 1.0) + scale.get(symbols[j], 1.0)) / 2.0
            if 0 < d[i, j] <= base_cutoff * s:
                adj[i, j] = adj[j, i] = 1
    return adj


def build_adjacency_knn(atoms: Atoms, k: int) -> np.ndarray:
    d = atoms.get_all_distances(mic=False)
    n = len(atoms)
    adj = np.zeros((n, n), dtype=int)
    for i in range(n):
        idx = np.argsort(d[i])[1 : k + 1]
        adj[i, idx] = 1
    return _to_dense_symmetric(adj)


def adjacency_sequence(frames: list[Atoms], method: str = "fixed", **kwargs) -> list[np.ndarray]:
    builders = {
        "fixed": lambda a: build_adjacency_fixed_cutoff(a, kwargs.get("cutoff", 3.1)),
        "element_scaled": lambda a: build_adjacency_element_scaled(a, kwargs.get("base_cutoff", 3.1), kwargs.get("scale", {})),
        "knn": lambda a: build_adjacency_knn(a, kwargs.get("k", 3)),
    }
    return [builders[method](f) for f in frames]
