import sys
import heapq


def dijkstra(start):
    costs[start] = 0

    heap = []
    heapq.heappush(heap, [costs[start], start])

    while heap:
        curr_cost, curr_dest = heapq.heappop(heap) # 최단 거리가 가장 짧은 노드를 꺼냄
        if costs[curr_dest] < curr_cost:
            continue

        for next_dest, next_cost in graph[curr_dest]:
            cost = curr_cost + next_cost
            if cost < costs[next_dest]: 
                costs[next_dest] = cost
                heapq.heappush(heap, [costs[next_dest], next_dest])


N = int(sys.stdin.readline()[:-1])
M = int(sys.stdin.readline()[:-1])
graph = [[] for _ in range(N+1)]
for m in range(M):
    start, end, cost = list(map(int, sys.stdin.readline()[:-1].split()))
    graph[start].append((end, cost))
    
costs = dict()
for i in range(1, N+1):
    costs[i] = int(10e9)

S, E = map(int, sys.stdin.readline()[:-1].split())
dijkstra(S)
print(costs[E])