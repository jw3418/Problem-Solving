import sys
from collections import deque

V, E = map(int, sys.stdin.readline().strip().split())

indegree = [0] * (V+1) #모든 노드에 대한 진입차수 0으로 초기화
graph = [[] for v in range(V+1)]
for e in range(E):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    indegree[v] += 1

def topology_sort():
    queue = deque()

    for v in range(1, V+1): #진입차수가 0인 노드를 큐에 삽입
        if indegree[v] == 0: queue.append(v)
    
    while queue:
        cur = queue.popleft()
        result.append(cur)

        for nex in graph[cur]:
            indegree[nex] -= 1
            if indegree[nex] == 0: queue.append(nex)

result = []
topology_sort()
print(" ".join(map(str, result)))