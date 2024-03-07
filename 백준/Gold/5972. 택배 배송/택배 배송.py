import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cur_di, cur = heapq.heappop(heap)
        if distances[cur] < cur_di: continue
        for nex, nex_di in graph[cur]:
            distance = cur_di + nex_di
            if distances[nex] > distance:
                distances[nex] = distance
                heapq.heappush(heap, (distance, nex))

N, M = map(int, input().strip().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c)); graph[b].append((a, c))

distances = [int(10e9) for n in range(N+1)]
dijkstra(1)
print(distances[N])