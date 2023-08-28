from itertools import permutations

def solution(k, dungeons):
    
    max_result = 0
    for dgs in tuple(permutations(dungeons)):
        local_k = k
        local_max_result = 0
        for dg in dgs:
            need, will_use = dg
            if need <= local_k:
                local_k -= will_use
                local_max_result += 1
            else:
                break

        max_result = max(max_result, local_max_result)
    return max_result
        