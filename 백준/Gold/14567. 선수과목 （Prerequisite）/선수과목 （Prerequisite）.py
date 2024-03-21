import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for n in range(N+1)]
indegree = [0]*(N+1)

for m in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    indegree[B] += 1

queue = deque([])
semester = [0]*(N+1)
for n in range(1, N+1):
    if indegree[n] == 0:
        queue.append((n, 1))
        semester[n] = 1

while queue:
    cur, cnt = queue.popleft()

    for nex in adj[cur]:
        indegree[nex] -= 1
        if indegree[nex] == 0:
            queue.append((nex, cnt+1))
            semester[nex] = cnt+1
print(" ".join(map(str, semester[1:])))