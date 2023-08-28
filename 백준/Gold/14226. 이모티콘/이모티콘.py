import sys
from collections import deque

def bfs():
    queue = deque([]); queue.append((1, 0))

    while queue:
        curr = queue.popleft()

        if curr[0] == S:
            print(visit[curr])
            return
        
        if (curr[0], curr[0]) not in visit:
            queue.append((curr[0], curr[0])); visit[(curr[0], curr[0])] = visit[curr] + 1
        if (curr[0]-1, curr[1]) not in visit:
            queue.append((curr[0]-1, curr[1])); visit[(curr[0]-1, curr[1])] = visit[curr] + 1
        if (curr[0]+curr[1], curr[1]) not in visit:
            queue.append((curr[0]+curr[1], curr[1])); visit[(curr[0]+curr[1], curr[1])] = visit[curr] + 1

   
S = int(input())

visit = dict()
visit[(1, 0)] = 0
bfs()