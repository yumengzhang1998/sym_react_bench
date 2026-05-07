import pandas as pd


def summarize_stability(raw_states: list[str], filtered_states: list[str]) -> pd.DataFrame:
    return pd.DataFrame([
        {"metric": "raw_unique", "value": len(set(raw_states))},
        {"metric": "filtered_unique", "value": len(set(filtered_states))},
        {"metric": "change_rate", "value": sum(a != b for a, b in zip(raw_states, filtered_states)) / max(len(raw_states), 1)},
    ])
