def solution(citations):
    N = len(citations)
    
    for h in range(max(citations), -1, -1):
        count = 0
        for j in range(N):
            if h <= citations[j]: count += 1
        
        if h <= count: return h