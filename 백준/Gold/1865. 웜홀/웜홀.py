import sys


def bellman_ford(graph, start):
    dist = dict()
    for node in graph:
        dist[node] = int(1e9)
    dist[start] = 0

    for i in range(N):
        for node in graph:
            for element in graph[node]:
                nnode, cost = element
                if dist[nnode] > dist[node] + cost:
                    dist[nnode] = dist[node] + cost
                    if i == N-1:
                        return True
    return False


TC = int(sys.stdin.readline()[:-1])
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline()[:-1].split())
    graph = dict()
    for m in range(M):
        S, E, T = map(int, sys.stdin.readline()[:-1].split())
        if S in graph: graph[S].append((E, T))
        else: graph[S] = [(E, T)]
        if E in graph: graph[E].append((S, T))
        else: graph[E] = [(S, T)]

    for w in range(W):
        S, E, T = map(int, sys.stdin.readline()[:-1].split())
        if S in graph: graph[S].append((E, -T))
        else: graph[S] = [(E, -T)]


    possible = bellman_ford(graph, 1)
    if possible: print("YES")
    else: print("NO")