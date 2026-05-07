# Topology-State Kinetics for Fluxional Bi/P Cluster Fusion Pathways

This repository provides a production-oriented Python package (`topokin`) for **topology-based kinetic analysis** of fluxional inorganic cluster trajectories (Bi/P-like systems).

## Scientific Motivation
Naive bond-change event counting overcounts thermal noise in fluxional clusters with ambiguous bonding. This package maps:

`R(t) -> A(t) -> D(t) -> S(t) -> metastable sequence -> transition network`

to deliver robust, interpretable topology-state kinetics.

## Key Statement
The benchmark uses chemically plausible Bi/P cluster motifs but controlled/artificial topology pathways. The benchmark is designed to test event definitions and topology-state kinetics, not to reproduce experimentally validated synthesis mechanisms.

## Descriptor Hierarchy
- Level 1: `(n3,n4,n5)`
- Level 2: `(n3,n4,n5,n6)`
- Level 3: `(n3,n4,n5,n6,n_edges,n_components,mean_degree)`
- Level 4: coordination histogram
- Level 5: graph-distance / clustering features

## Features
- Structure-realistic synthetic topology-hopping generator.
- Adjacency builders (fixed cutoff, element-scaled, kNN).
- Primitive/chordless ring counting up to configurable ring size.
- Temporal filtering (minimum lifetime, moving-majority, hysteresis).
- Kinetic transition-network analysis.
- Fusion precursor and gateway enrichment.
- Baselines: bond-event, coordination-event, RMSD clustering, graph-feature clustering.
- Robustness benchmarking under perturbations.
- Publication-ready figure generation (PNG/PDF).

## Installation
```bash
pip install -e .
```

## CLI
```bash
python -m topokin.cli.generate_synthetic --config configs/synthetic_bi.yaml
python -m topokin.cli.analyze_trajectory --config configs/default.yaml --trajectory data/synthetic/demo/trajectory.xyz
python -m topokin.cli.run_benchmark --config configs/benchmark.yaml
python -m topokin.cli.summarize_results --results results/analysis_summary.json
```

## Real Bi11 Interface
Real trajectories are optional and not required for initial use. Use `data/real_placeholder/` and `configs/real_bi11_template.yaml` as integration templates.
