import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [[] for n in range(N+1)]
indegree = [0]*(N+1)
for m in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for n in range(1, N+1):
    if indegree[n] == 0: heapq.heappush(heap, n)

result = []
while heap:
    cur = heapq.heappop(heap)
    result.append(cur)

    for nex in graph[cur]:
        indegree[nex] -= 1
        if indegree[nex] == 0: heapq.heappush(heap, nex)

print(" ".join(map(str, result)))