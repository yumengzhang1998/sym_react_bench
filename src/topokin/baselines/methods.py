import numpy as np


def bond_event_baseline(adj_seq: list[np.ndarray]) -> list[int]:
    return [int(np.sum(np.abs(b - a)) // 2) for a, b in zip(adj_seq[:-1], adj_seq[1:])]
