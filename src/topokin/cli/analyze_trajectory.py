import argparse
import json
from pathlib import Path

import pandas as pd
from ase.io import read

from topokin.config import load_config
from topokin.graph.adjacency import adjacency_sequence
from topokin.kinetics.analysis import transition_matrix
from topokin.states.descriptors import descriptor_from_adjacency


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--trajectory", required=True)
    args = p.parse_args()
    cfg = load_config(args.config)
    frames = read(args.trajectory, index=":")
    adjs = adjacency_sequence(frames, method=cfg.get("adjacency_method", "fixed"), cutoff=cfg.get("cutoff", 3.1))
    states = [str(descriptor_from_adjacency(a, level=cfg.get("descriptor_level", 1)).values) for a in adjs]
    tm = transition_matrix(states)
    Path("results").mkdir(exist_ok=True)
    tm.to_csv("results/transition_matrix.csv")
    Path("results/analysis_summary.json").write_text(json.dumps({"n_frames": len(states), "n_states": len(set(states))}, indent=2), encoding="utf-8")
    print(pd.Series(states).value_counts().head())


if __name__ == "__main__":
    main()
