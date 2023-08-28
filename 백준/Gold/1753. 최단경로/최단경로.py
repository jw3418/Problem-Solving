import sys
import heapq

def dijkstra(start):
    global distances
    distances[start] = 0

    heap = []
    heapq.heappush(heap, [distances[start], start])

    while heap:
        curr_distance, curr_dest = heapq.heappop(heap) #최단 거리가 가장 짧은 노드 꺼냄
        if distances[curr_dest] < curr_distance:
            continue

        for new_dest, new_distance in graph[curr_dest]:
            distance = curr_distance + new_distance
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(heap, [distance, new_dest])
    
V, E = map(int, sys.stdin.readline()[:-1].split()); K = int(sys.stdin.readline()[:-1])

graph = [[] for _ in range(V+1)]
for e in range(E):
    u, v, w = list(map(int, sys.stdin.readline()[:-1].split()))
    graph[u].append((v, w))

distances = dict()
for v in range(1, V+1):
    distances[v] = int(10e9)

dijkstra(K)

for key, value in distances.items():
    if value == int(10e9):
        print("INF")
    else:
        print(value)