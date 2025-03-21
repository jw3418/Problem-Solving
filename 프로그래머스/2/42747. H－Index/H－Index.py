def solution(citations):
    N = len(citations); citations.sort(reverse=True)
    
    h_idx = max(citations)
    while h_idx >= 0:
        l, s = 0, 0
        for c in citations:
            if c >= h_idx: l += 1
            else: s += 1
        if l >= h_idx and s <= h_idx: return h_idx
        else: h_idx -= 1