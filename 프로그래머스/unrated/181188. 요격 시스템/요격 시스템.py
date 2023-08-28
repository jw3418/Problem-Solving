def solution(targets):
    targets.sort()
    
    curr = 0; count = 0
    for s, e in targets:
        if curr > s:
            curr = min(curr, e)
        else:
            curr = e
            count += 1
            
    return count