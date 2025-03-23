def solution(participant, completion):
    P = dict()
    for p in participant:
        if p in P: P[p] += 1
        else: P[p] = 1
    for c in completion:
        P[c] -= 1
    ans = ""
    for key, value in P.items():
        if value > 0: ans = key
    return ans