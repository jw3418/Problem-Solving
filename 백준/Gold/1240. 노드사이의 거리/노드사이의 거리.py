import sys

N, M = map(int, sys.stdin.readline()[:-1].split())
edges = dict()
for n in range(N-1):
    a, b, cost = map(int, sys.stdin.readline()[:-1].split())
    if a in edges: edges[a].append((b, cost))
    else: edges[a] = [(b, cost)]
    if b in edges: edges[b].append((a, cost))
    else: edges[b] = [(a, cost)]

nodes = []
for m in range(M): nodes.append(list(map(int, sys.stdin.readline()[:-1].split())))

def dfs(node, dest, local_cost):
    global global_cost
    visit[node] = True
    if node == dest:
        global_cost = max(global_cost, local_cost)
        return
    for nnode, cost in edges[node]:
        if not visit[nnode]:
            dfs(nnode, dest, local_cost + cost)

for node in nodes:
    src, dest = node
    global_cost = 0
    visit = [False]*(N+1)
    dfs(src, dest, 0)
    print(global_cost)