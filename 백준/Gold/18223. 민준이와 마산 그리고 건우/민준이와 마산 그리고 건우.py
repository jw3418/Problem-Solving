import sys
import heapq
input = sys.stdin.readline

V, E, P = map(int, input().split())
graph = [[] for v in range(V+1)]
for e in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(s, distance):
    distance[s] = 0

    heap = []
    heapq.heappush(heap, [distance[s], s])

    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist: continue

        for nex, ndist in graph[cur]:
            tdist = dist + ndist
            if tdist < distance[nex]:
                distance[nex] = tdist
                heapq.heappush(heap, [distance[nex], nex])

distance1 = [int(10e9) for v in range(V+1)]
dijkstra(1, distance1)
distance2 = [int(10e9) for v in range(V+1)]
dijkstra(P, distance2)

# print(distance1); print(distance2)

if distance1[V] == distance1[P]+distance2[V]: print("SAVE HIM")
else: print("GOOD BYE")