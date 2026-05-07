import pandas as pd


def precursor_enrichment(states: list[str], event_labels: list[str], pre_label: str = "fusion_like_closure") -> pd.DataFrame:
    s = pd.Series(states)
    e = pd.Series(event_labels)
    pre_mask = e.shift(-1).eq(pre_label).fillna(False)
    p_pre = s[pre_mask].value_counts(normalize=True)
    p_all = s.value_counts(normalize=True)
    df = pd.DataFrame({"p_pre": p_pre, "p_all": p_all}).fillna(0)
    df["enrichment"] = df["p_pre"] / df["p_all"].replace(0, 1)
    return df.sort_values("enrichment", ascending=False)
