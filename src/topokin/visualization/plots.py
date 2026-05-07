from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_transition_matrix_plot(matrix: pd.DataFrame, outstem: str) -> None:
    Path(outstem).parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(4, 4))
    im = ax.imshow(matrix.values)
    ax.set_xticks(range(len(matrix.columns)), matrix.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(matrix.index)), matrix.index)
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(f"{outstem}.png", dpi=200)
    fig.savefig(f"{outstem}.pdf")
    plt.close(fig)
