import sys
import heapq

def dijkstra(start):
    distances = dict()
    for n in range(N+1):
        distances[n] = int(10e9)
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

    return distances
    
N, M, X = map(int, sys.stdin.readline()[:-1].split())
graph = [[] for _ in range(N+1)]
for m in range(M):
    start, end, time = list(map(int, sys.stdin.readline()[:-1].split()))
    graph[start].append((end, time))

result = 0
result_pre = dijkstra(X)
for i in range(1, N+1):
    result_post = dijkstra(i)
    result = max(result, result_pre[i] + result_post[X])
print(result)