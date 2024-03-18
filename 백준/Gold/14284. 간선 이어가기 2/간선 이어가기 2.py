import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().strip().split())
adj = [[] for n in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().strip().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
S, T = map(int, input().strip().split())

costs = [int(10e9)]*(N+1); costs[S] = 0
heap = []; heapq.heappush(heap, (0, S))

while heap:
    cur_cost, cur = heapq.heappop(heap)
    if costs[cur] < cur_cost: continue
    for nex, nex_cost in adj[cur]:
        cost = cur_cost + nex_cost
        if cost < costs[nex]:
            costs[nex] = cost
            heapq.heappush(heap, (cost, nex))
print(costs[T])