def similarity(a, b):
    if not a or not b:
        return 0

    a = a.lower()
    b = b.lower()

    score = 0

    if a == b:
        score += 5

    if a in b or b in a:
        score += 3

    wa = set(a.split())
    wb = set(b.split())

    score += len(wa & wb) * 2
    return score


def rank_causes(ai_causes, kdf_causes):
    best = None
    best_score = -1

    for cause in kdf_causes:
        label = cause.get("label", "")
        for ai in ai_causes:
            s = similarity(ai, label)
            if s > best_score:
                best_score = s
                best = cause

    return best