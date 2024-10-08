import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

def dijkstra(s, broken=None):
    heap = []; heapq.heappush(heap, (0, s))
    distance = [[int(10e9), -1] for n in range(N+1)]; distance[s][0] = 0; distance[s][1] = s #distance 배열에 preve node를 같이 저장

    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur][0] < dist: continue
        for nex, ndist in graph[cur]:
            if (cur, nex) == broken or (nex, cur) == broken: continue
            if distance[nex][0] > ndist + dist:
                distance[nex][0] = ndist + dist; distance[nex][1] = cur
                heapq.heappush(heap, (ndist + dist, nex))
    return distance

vdistance = dijkstra(1)
ans = 0
cur = N
while cur != 1:
    prev = vdistance[cur][1]
    vdistance = dijkstra(1, (cur, prev))
    ans = max(ans, vdistance[N][0])
    cur = prev
print(ans)