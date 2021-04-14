def latest(scores):
    return scores[-1]


def personal_best(scores):
    for a in [scores]:
        return max(a)


def personal_top_three(scores):
    list_scores = sorted(scores, reverse=True)
    return list_scores[:3]

