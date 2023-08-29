from collections import deque

def solution(begin, target, words):
    N = len(begin)
    
    if target not in words:
        return 0
    
    queue = deque([]); queue.append((begin, 0))
    visit = set(); visit.add(begin)
    
    while queue:
        src, cnt = queue.popleft()
        if src == target:
            return cnt
        
        for word in words:
            check = 0
            for i in range(N):
                if word[i] == src[i]: check += 1
            if check == N-1:
                visit.add(word)
                queue.append((word, cnt+1))
        
    return 0