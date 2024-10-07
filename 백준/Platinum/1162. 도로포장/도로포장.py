import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(s):
    heap = []; heapq.heappush(heap, (0, s, 0)) #dist, node, 포장횟수
    distance[s][0] = 0

    while heap:
        dist, cur, cnt = heapq.heappop(heap)
        if distance[cur][cnt] < dist: continue
        for nex, ndist in graph[cur]:
            ndist = ndist+dist
            if distance[nex][cnt] > ndist:
                distance[nex][cnt] = ndist
                heapq.heappush(heap, (ndist, nex, cnt))
            if cnt < K and distance[nex][cnt+1] > dist:
                distance[nex][cnt+1] = dist
                heapq.heappush(heap, (dist, nex, cnt+1))

distance = [[int(10e9) for k in range(K+1)] for n in range(N+1)]; distance[1][0] = 0
dijkstra(1)
print(min(distance[N]))