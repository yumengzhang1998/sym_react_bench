from collections import Counter


def minimum_lifetime_filter(states: list[str], min_lifetime: int = 2) -> list[str]:
    out = states[:]
    n = len(states)
    i = 0
    while i < n:
        j = i
        while j < n and states[j] == states[i]:
            j += 1
        if j - i < min_lifetime:
            fill = out[i - 1] if i > 0 else (out[j] if j < n else out[i])
            for k in range(i, j):
                out[k] = fill
        i = j
    return out


def moving_window_majority(states: list[str], window: int = 3) -> list[str]:
    half = window // 2
    out = []
    for i in range(len(states)):
        chunk = states[max(0, i - half): min(len(states), i + half + 1)]
        out.append(Counter(chunk).most_common(1)[0][0])
    return out
