from collections import deque

def solution(x, y, n):
    
    def bfs(x):
        queue = deque([]); queue.append((x, 0))
        visit = set(); visit.add(x)
        
        while queue:
            src, cnt = queue.popleft()
            if src == y:
                return cnt
            
            dest = src + n
            if dest not in visit and dest <= y:
                visit.add(dest)
                queue.append((dest, cnt+1))
                
            dest = src * 2    
            if dest not in visit and dest <= y:
                visit.add(dest)
                queue.append((dest, cnt+1))
                
            dest = src * 3
            if dest not in visit and dest <= y:
                visit.add(dest)
                queue.append((dest, cnt+1))
                
        return -1
    
    result = bfs(x)
    return result