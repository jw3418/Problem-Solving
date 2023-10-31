import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for n in range(N+1)]; root = []
indegree = [0] * (N+1)
for m in range(M):
    tmp = list(map(int, sys.stdin.readline().strip().split())); tmp = tmp[1:]
    for i in range(len(tmp)-1): graph[tmp[i]].append(tmp[i+1]); indegree[tmp[i+1]] += 1
    root.append(tmp[0])

def topology_sort():
    queue = deque()

    for n in range(1, N+1):
        if indegree[n] == 0: queue.append(n)
    
    while queue:
        cur = queue.popleft()
        result.append(cur)

        for nex in graph[cur]:
            indegree[nex] -= 1
            if indegree[nex] == 0: queue.append(nex)

result = []
topology_sort()
if len(result) != N: print(0)
else:
    for r in result: print(r)