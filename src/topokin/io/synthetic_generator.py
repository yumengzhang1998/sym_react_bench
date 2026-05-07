from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from ase import Atoms
from ase.io import write



def _ring_coords(n: int, r: float, z: float = 0.0) -> np.ndarray:
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.c_[r * np.cos(t), r * np.sin(t), np.full(n, z)]


def built_in_motif(name: str, element: str = "Bi") -> Atoms:
    bl = 3.1 if element == "Bi" else 2.2
    if name in {"P7_cage", "Bi7_compact"}:
        pos = _ring_coords(6, bl) ; pos = np.vstack([pos, [[0, 0, 0.8 * bl]]])
    elif name in {"P8_cage", "Bi9_compact"}:
        pos = np.vstack([_ring_coords(4, bl, -0.5 * bl), _ring_coords(4, bl, 0.5 * bl)])
        if "9" in name: pos = np.vstack([pos, [[0, 0, 0]]])
    elif name in {"P10_cage", "P12_cage", "Bi11_compact"}:
        n = 10 if "10" in name else 12 if "12" in name else 11
        pos = _ring_coords(n, 1.1 * bl)
    elif "opened" in name:
        pos = _ring_coords(8, bl); pos[0] += np.array([1.5 * bl, 0, 0])
    else:
        pos = np.c_[np.linspace(-bl, bl, 7), np.zeros(7), np.zeros(7)]
    return Atoms(symbols=[element] * len(pos), positions=pos)


def generate_dataset(dataset_dir: str, element: str = "Bi", frames: int = 60, seed: int = 0) -> Path:
    rng = np.random.default_rng(seed)
    out = Path(dataset_dir)
    (out / "motifs").mkdir(parents=True, exist_ok=True)
    motifs = {"A": built_in_motif("Bi7_compact" if element == "Bi" else "P7_cage", element), "B": built_in_motif("opened_Bi_cage" if element == "Bi" else "opened_P_cage", element)}
    for k, v in motifs.items():
        write(out / "motifs" / f"motif_{k}.xyz", v)
    states = ["A"] * (frames // 3) + ["B"] * (frames // 6) + ["A"] * (frames - (frames // 3 + frames // 6))
    xyz_frames = []
    rows = []
    for i, s in enumerate(states):
        atoms = motifs[s].copy()
        atoms.positions += rng.normal(0, 0.05, size=atoms.positions.shape)
        xyz_frames.append(atoms)
        rows.append({"frame": i, "state_label": s, "event_label": "thermal_noise" if i % 10 else "short_transient", "segment_id": i // 10, "motif_label": s})
    write(out / "trajectory.xyz", xyz_frames)
    pd.DataFrame(rows).to_csv(out / "ground_truth_events.csv", index=False)
    metadata = {
        "dataset_name": out.name, "element": element, "n_atoms": len(xyz_frames[0]), "n_frames": frames,
        "motif_names": list(motifs), "motif_source": "built-in plausible motifs", "generation_mode": "controlled_topology_hopping",
        "random_seed": seed, "warning": "Controlled benchmark pathways; not experimentally validated mechanisms."
    }
    (out / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (out / "config.yaml").write_text(yaml.safe_dump({"element": element, "frames": frames, "seed": seed}), encoding="utf-8")
    return out
