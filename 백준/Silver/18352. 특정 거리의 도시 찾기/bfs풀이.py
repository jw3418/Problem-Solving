import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline()[:-1].split())
graph = dict()
for m in range(M):
    A, B = map(int, sys.stdin.readline()[:-1].split())
    if A in graph: graph[A].append(B)
    else: graph[A] = [B]

def bfs(start):
    global flag
    queue = deque([]); queue.append((start, 0))
    visit = set(); visit.add(start)

    while queue:
        curr, cnt = queue.popleft()
        if cnt == K: answer.append(curr)
        
        if curr in graph:
            for next in graph[curr]:
                if next not in visit:
                    visit.add(next)
                    queue.append((next, cnt+1))

answer = []
bfs(X)
if not answer: print(-1)
else:
    answer.sort()
    for a in answer: print(a)
