import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(N+1): graph[i].sort(reverse=True)

queue = deque([])
queue.append(R)
visit = [False]*(N+1); visit[R] = True
order = [0]*(N+1)
cnt = 1
while queue:
    cur = queue.popleft()
    order[cur] = cnt; cnt+=1
    for nex in graph[cur]:
        if not visit[nex]:
            visit[nex] = True
            queue.append(nex)
order = order[1:]
for o in order:
    print(o)