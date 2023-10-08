import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

while True:
    M, N = map(int, sys.stdin.readline()[:-1].split())
    if (M, N) == (0, 0): break

    edges = []; tc = 0
    for n in range(N):
        x, y, z = map(int, sys.stdin.readline()[:-1].split()); tc += z
        edges.append((x, y, z))

    edges.sort(key=lambda x:x[2])
    parent = [i for i in range(M)]

    mtc = 0
    for edge in edges:
        u, v, cost = edge
        if find(u) != find(v):
            mtc += cost; union(u, v)
    print(tc - mtc)