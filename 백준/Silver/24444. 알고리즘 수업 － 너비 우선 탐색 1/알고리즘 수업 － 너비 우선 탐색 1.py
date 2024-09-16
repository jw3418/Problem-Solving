import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for n in range(1, N+1): graph[n].sort()

queue = deque([]); queue.append(R)
visit = [False] * (N+1); visit[R] = True
result = [0] * (N+1); cnt = 1
while queue:
    cur = queue.popleft()
    result[cur] = cnt; cnt += 1
    for nex in graph[cur]:
        if not visit[nex]:
            queue.append(nex)
            visit[nex] = True
result = result[1:]
for n in range(N): print(result[n])