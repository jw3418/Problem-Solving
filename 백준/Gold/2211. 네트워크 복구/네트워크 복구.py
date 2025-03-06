import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for m in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

def dijkstra(start):
    global result
    result[start][0] = 0

    heap = []; heapq.heappush(heap, [result[start][0], start])
    while heap:
        cur_dist, cur = heapq.heappop(heap)
        if result[cur][0] < cur_dist: continue
        for nex, nex_dist in graph[cur]:
            tdist = cur_dist + nex_dist
            if tdist < result[nex][0]:
                result[nex][0] = tdist
                result[nex][1] = cur
                heapq.heappush(heap, [tdist, nex])

result = dict()
for n in range(N+1): result[n] = [int(10e9), n]
dijkstra(1)

edges = []
for i in range(2, N+1):
    cur = i
    while True:
        edges.append((result[cur][1], cur))
        cur = result[cur][1]
        if cur == 1: break
edges = list(set(edges))
print(len(edges))
for edge in edges:
    print(" ".join(map(str, edge)))