import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
bridge = [[] for n in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().split())
    bridge[a].append((c, b))
    bridge[b].append((c, a))
for n in range(N+1): bridge[n].sort(reverse=True)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, cur = heapq.heappop(heap); dist = -dist

        if dist < distance[cur]: continue
        for ndist, nex in bridge[cur]:
            if dist == 0:
                distance[nex] = ndist
                heapq.heappush(heap, (-distance[nex], nex))
            elif distance[nex] < ndist and distance[nex] < dist:
                distance[nex] = min(ndist, dist)
                heapq.heappush(heap, (-distance[nex], nex))

distance = [0]*(N+1)
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])