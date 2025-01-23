import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = dict()
for n in range(N-1):
    p, q, r = map(int, input().split())
    if p in graph: graph[p].append((q, r))
    else: graph[p] = [(q, r)]
    if q in graph: graph[q].append((p, r))
    else: graph[q] = [(p, r)]

for q in range(Q):
    K, V = map(int, input().split())

    queue = deque([]); queue.append((V, int(10e9)))
    visit = set(); visit.add(V)

    cnt = -1
    while queue:
        cv, ck = queue.popleft()
        cnt += 1
        for nv, nk in graph[cv]:
            nk = min(nk, ck)
            if nk >= K:
                if nv not in visit:
                    visit.add(nv)
                    queue.append((nv, nk))
    print(cnt)