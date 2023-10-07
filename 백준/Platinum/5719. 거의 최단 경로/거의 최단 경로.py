import sys
import heapq
from collections import deque

def dijkstra(S, D):
    global edges, edges_check

    dists = [int(10e9)] * N; dists[S] = 0
    heap = []
    heapq.heappush(heap, [dists[S], S])

    while heap:
        curr_dist, curr = heapq.heappop(heap)
        if dists[curr] < curr_dist: continue

        if curr in edges:
            for next, next_dist in edges[curr]:
                distance = curr_dist + next_dist
                if distance < dists[next] and edges_check[curr][next]:
                    dists[next] = distance
                    heapq.heappush(heap, [distance, next])
    return dists

while True:
    N, M = map(int, sys.stdin.readline()[:-1].split())
    if N == 0 and M == 0: break

    S, D = map(int, sys.stdin.readline()[:-1].split())

    edges = dict()
    edges_r = dict()
    edges_check = [[False]*N for n in range(N)] #경로의 일부를 공유하는 경우를 처리하기 위해 인접행렬 선언

    for m in range(M):
        U, V, P = map(int, sys.stdin.readline()[:-1].split())
        if U in edges: edges[U].append((V, P))
        else: edges[U] = [(V, P)]
        if V in edges_r: edges_r[V].append((U, P))
        else: edges_r[V] = [(U, P)]
        edges_check[U][V] = True

    dists1 = dijkstra(S, D)
    if not dists1: print(-1); continue #최단경로가 존재하지 않는 경우 예외처리
    min_distance = dists1[D]

    # bfs 역추적으로 최단 경로 제거
    queue = deque([]); queue.append((0, D))
    while queue:
        curr_dist, curr = queue.popleft()
        if curr in edges_r:
            for next, next_dist in edges_r[curr]:
                distance = curr_dist + next_dist
                if distance + dists1[next] == min_distance:
                    if edges_check[next][curr]:
                        edges_check[next][curr] = False #최단 경로 제거
                        queue.append((distance, next))

    dists2 = dijkstra(S, D)
    if not dists2: print(-1)
    else:
        if dists2[D] == int(10e9): print(-1)
        else: print(dists2[D])