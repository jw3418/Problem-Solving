import sys
import heapq
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[(d+1, 1)] for d in range(D)]; graph.append([])
for n in range(N):
    s, e, l = map(int, input().split())
    if e <= D: graph[s].append((e, l))


dist = [int(10e9) for d in range(D+1)]

heap = []; dist[0] = 0
heapq.heappush(heap, (dist[0], 0))

while heap:
    cur_l, cur = heapq.heappop(heap)
    if dist[cur] < cur_l: continue

    for nex, nex_l in graph[cur]:
        length = cur_l + nex_l
        if length < dist[nex]:
            dist[nex] = length
            heapq.heappush(heap, (dist[nex], nex))
                
print(dist[D])