import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = dict()
for m in range(M):
    a, b = map(int, input().split())
    if a in graph: graph[a].append(b)
    else: graph[a] = [b]
    if b in graph: graph[b].append(a)
    else: graph[b] = [a]

queue = deque([]); queue.append(1) # (헛간 번호, 거리)
visit = [0] * (N+1); visit[1] += 1
while queue:
    cur = queue.popleft()
    for nex in graph[cur]:
        if not visit[nex]:
            visit[nex] = visit[cur] + 1
            queue.append(nex)

max_ = max(visit); cnt = 0; flag = 0
for i in range(1, N+1):
    if max_ == visit[i]:
        cnt += 1
        if not flag:
            flag = i
print(flag, max_-1, cnt)