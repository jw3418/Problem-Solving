def solution(N, lost, reserve):
    nlost = list(set(lost) - set(reserve))
    nreserve = list(set(reserve) - set(lost))
    lost = nlost; reserve = nreserve
    
    ans = N
    for i in range(1, N+1):
        if i in lost:
            if i-1 in reserve: reserve.remove(i-1)
            elif i+1 in reserve: reserve.remove(i+1)
            else: ans -= 1
    return ans