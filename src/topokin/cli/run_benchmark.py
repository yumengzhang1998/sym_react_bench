import argparse
from pathlib import Path

import pandas as pd

from topokin.benchmarks.robustness import summarize_stability


def main() -> None:
    argparse.ArgumentParser().parse_args()
    out = summarize_stability(["A", "A", "B", "A"], ["A", "A", "A", "A"])
    Path("results").mkdir(exist_ok=True)
    out.to_csv("results/benchmark_summary.csv", index=False)
    print(out)


if __name__ == "__main__":
    main()
