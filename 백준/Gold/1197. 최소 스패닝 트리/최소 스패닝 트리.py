import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

V, E = map(int, sys.stdin.readline()[:-1].split())
edges = []
for e in range(E):
    A, B, C = map(int, sys.stdin.readline()[:-1].split())
    edges.append((A, B, C))
edges.sort(key=lambda x:x[2])

parent = [i for i in range(V+1)]

total_cost = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        total_cost += cost
        union_parent(parent, a, b)
print(total_cost)