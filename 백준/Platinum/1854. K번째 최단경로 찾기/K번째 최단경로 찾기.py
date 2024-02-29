import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    heapq.heappush(heap, (0, start))
    distances[start][0] = 0
    
    while heap:
        cur_di, cur = heapq.heappop(heap)
        for nex, nex_di in graph[cur]:
            distance = cur_di + nex_di
            if distance < distances[nex][K-1]:
                distances[nex][K-1] = distance
                distances[nex].sort()
                heapq.heappush(heap, (distance, nex))

N, M, K = map(int, input().strip().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))

heap = []
distances = [[int(10e9)]*K for n in range(N+1)] #distances 배열을 2차원으로 선언
dijkstra(1)

for i in range(1, N+1):
    if distances[i][K-1] == int(10e9): print(-1)
    else: print(distances[i][K-1])