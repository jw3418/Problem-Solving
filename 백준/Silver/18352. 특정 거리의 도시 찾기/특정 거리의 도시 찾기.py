import sys
import heapq

N, M, K, X = map(int, sys.stdin.readline()[:-1].split())
graph = dict()
for m in range(M):
    A, B = map(int, sys.stdin.readline()[:-1].split())
    if A in graph: graph[A].append(B)
    else: graph[A] = [B]

def dijkstra(start):
    global distances
    distances[start] = 0

    heap = []
    heapq.heappush(heap, [distances[start], start])

    while heap:
        curr_distance, curr = heapq.heappop(heap)
        if distances[curr] < curr_distance: continue

        if curr in graph:
            for next in graph[curr]:
                next_distance = curr_distance + 1
                if next_distance < distances[next]:
                    distances[next] = next_distance
                    heapq.heappush(heap, [next_distance, next])

distances = dict()
for i in range(1, N+1): distances[i] = int(10e9)

dijkstra(X)

answer = []
for key, value in distances.items():
    if value == K: answer.append(key)
answer.sort()
if not answer: print(-1)
else:
    for a in answer:
        print(a)