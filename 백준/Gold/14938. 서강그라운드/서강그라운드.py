import sys
import heapq

def dijkstra(start):
    costs = dict()
    for v in range(1, N+1): costs[v] = int(10e9)
    costs[start] = 0

    heap = []
    heapq.heappush(heap, [costs[start], start])

    while heap:
        cost, node = heapq.heappop(heap)
        if costs[node] < cost or node not in edges: continue

        for nnode, ncost in edges[node]:
            tcost = cost + ncost
            if tcost < costs[nnode]:
                costs[nnode] = tcost
                heapq.heappush(heap, [tcost, nnode])
    
    count = 0
    for key, value in costs.items():
        if value <= M: count += items[key]
    return count

N, M, R = map(int, sys.stdin.readline()[:-1].split())
items = dict(); tmp = list(map(int, sys.stdin.readline()[:-1].split()))
for i in range(1, N+1): items[i] = tmp[i-1]

edges = dict()
for r in range(R):
    a, b, l = map(int, sys.stdin.readline()[:-1].split())
    if a in edges: edges[a].append((b, l))
    else: edges[a] = [(b, l)]
    if b in edges: edges[b].append((a, l))
    else: edges[b] = [(a, l)]

answer = 0
for n in range(1, N+1):
    answer = max(answer, dijkstra(n))
print(answer)