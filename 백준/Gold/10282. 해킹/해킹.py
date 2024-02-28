import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    global distances
    distances[start] = 0

    heap = []
    heapq.heappush(heap, (distances[start], start))

    while heap:
        cur_di, cur = heapq.heappop(heap)
        if distances[cur] < cur_di: continue
        for nex, nex_di in graph[cur]:
            distance = cur_di + nex_di
            if distance < distances[nex]:
                distances[nex] = distance
                heapq.heappush(heap, (distance, nex))

T = int(input().strip())
for t in range(T):
    N, D, C = map(int, input().strip().split())
    graph = [[] for n in range(N+1)]
    for d in range(D):
        a, b, s = map(int, input().strip().split())
        graph[b].append((a, s))
    
    distances = dict()
    for n in range(1, N+1): distances[n] = int(10e9)

    dijkstra(C)
    cnt = 0; max_ = 0
    for dist in distances.values():
        if dist < int(10e9): cnt+=1; max_ = max(max_, dist)
    print(" ".join(map(str, [cnt, max_])))