import sys
import heapq


def dijkstra(start):
    distances = [int(10e9) for _ in range(N+1)]
    distances[start] = 0
    heap = []
    heapq.heappush(heap, [distances[start], start])

    while heap:
        curr_dist, curr = heapq.heappop(heap)
        if distances[curr] < curr_dist: continue
        for next, next_dist in graph[curr]:
            dist = curr_dist + next_dist
            if distances[next] > dist:
                distances[next] = dist
                heapq.heappush(heap, [distances[next], next])
    return distances

N, E = map(int, sys.stdin.readline()[:-1].split())
graph = [[] for _ in range(N+1)]
for e in range(E):
    a, b, c = map(int, sys.stdin.readline()[:-1].split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline()[:-1].split())

distance0 = dijkstra(1)
distance1 = dijkstra(v1)
distance2 = dijkstra(v2)

# 1 -> v1 -> v2 -> N
v1v2 = distance0[v1] + distance1[v2] + distance2[N]
# 1 -> v2 -> v1 -> N
v2v1 = distance0[v2] + distance2[v1] + distance1[N]

result = min(v1v2, v2v1)
if result >= int(10e9): print(-1)
else: print(result)