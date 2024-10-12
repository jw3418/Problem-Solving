import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijsktra(s):
    heap = []; heapq.heappush(heap, (0, s))
    distance = [int(10e9)] * (N+1); distance[s] = 0
    route = [0] * (N+1)
    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist: continue
        for nex, ndist in graph[cur]:
            ndist = dist + ndist
            if ndist < distance[nex]:
                distance[nex] = ndist
                heapq.heappush(heap, (ndist, nex))
                route[nex] = cur

    for i in range(1, N+1):
        if i == s: continue
        cur = i
        while result[s][i] == '-':
            if route[cur] == s: result[s][i] = cur
            else: cur = route[cur]

result = [['-'] * (N+1) for n in range(N+1)]
for n in range(1, N+1): dijsktra(n)

for n in range(1, N+1): print(" ".join(map(str, result[n][1:])))