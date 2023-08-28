import sys
import heapq


def dijstra(start):
    costs[start][0] = 0
    heap = []
    heapq.heappush(heap, [costs[start][0], start])

    while heap:
        curr_cost, curr = heapq.heappop(heap)
        if costs[curr][0] < curr_cost: continue
        for next, next_cost in graph[curr]:
            cost = curr_cost + next_cost
            if costs[next][0] > cost:
                costs[next][0] = cost
                costs[next][1] = curr #부모노드 저장
                heapq.heappush(heap, [costs[next][0], next])


N = int(sys.stdin.readline()[:-1]); M = int(sys.stdin.readline()[:-1])
graph = dict()
for n in range(1, N+1):
    graph[n] = []
for m in range(M):
    S, E, cost = map(int, sys.stdin.readline()[:-1].split())
    graph[S].append((E, cost))

costs = dict()
for n in range(1, N+1):
    costs[n] = [int(10e9), n]

S, E = map(int, sys.stdin.readline()[:-1].split())
dijstra(S)
print(costs[E][0])

path = []; dest = E
while True:
    pre_node = costs[dest][1]
    if pre_node == S:
        break
    path.append(pre_node)
    dest = pre_node

print(len(path) + 2)
print(S, end=" ")
for i in range(len(path)-1, -1, -1):
    print(path[i], end=" ")
print(E, end=" ")
print()