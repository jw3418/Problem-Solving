from collections import defaultdict

def solution(k, tangerine):
    
    count = defaultdict(int)
    for i in range(len(tangerine)):
        count[tangerine[i]] += 1
    
    count = list(count.items())
    count.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(count)):
        k -= count[i][1]
        if k <= 0: break
        
    return i+1