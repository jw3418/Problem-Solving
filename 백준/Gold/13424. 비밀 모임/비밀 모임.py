import sys
import heapq
input = sys.stdin.readline

def dijkstra(cur):
    distance[cur] = 0
    heap = []
    heapq.heappush(heap, (0, cur))

    while heap:
        dist, cur = heapq.heappop(heap)
        if dist > distance[cur]: continue
        for nex in graph[cur]:
            nex_dist = dist + nex[1]
            if nex_dist < distance[nex[0]]:
                distance[nex[0]] = nex_dist
                heapq.heappush(heap, (distance[nex[0]], nex[0]))

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    graph = [[] for n in range(N+1)]
    for m in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    K = int(input())
    friends = list(map(int, input().split()))

    total_distance = [0] * (N+1)
    for f in friends:
        distance = [int(10e9)] * (N+1)
        dijkstra(f)
        for i in range(N+1):
            total_distance[i] += distance[i]

    ans = 0
    min_ = int(10e9)
    for i in range(1, N+1):
        if min_ > total_distance[i]:
            min_ = total_distance[i]
            ans = i
    print(ans)