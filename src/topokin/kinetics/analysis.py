import pandas as pd


def transition_matrix(states: list[str]) -> pd.DataFrame:
    uniq = sorted(set(states))
    m = pd.DataFrame(0, index=uniq, columns=uniq)
    for a, b in zip(states[:-1], states[1:]):
        m.loc[a, b] += 1
    return m
