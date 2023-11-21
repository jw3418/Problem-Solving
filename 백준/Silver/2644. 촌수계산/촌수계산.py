import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A, B = map(int, sys.stdin.readline().strip().split())
M = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y); graph[y].append(x)

def dfs(cur, depth):
    depth += 1
    visit[cur] = True

    if cur == B: result.append(depth)

    for nex in graph[cur]:
        if not visit[nex]:
            dfs(nex, depth)

visit = [False] * (N+1)
result = []
dfs(A, 0)
if result: print(result[0] - 1)
else: print(-1)