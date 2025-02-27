def solution(keymap, targets):
    results = []
    K = dict()
    for key in keymap:
        for i in range(len(key)):
            if key[i] in K: K[key[i]] = min(i+1, K[key[i]])
            else: K[key[i]] = i+1
    # print(K)
    for target in targets:
        result = 0
        for t in target:
            if t not in K:
                result = -1
                break
            result += K[t]
        results.append(result)
    return results