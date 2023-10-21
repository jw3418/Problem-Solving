import sys
import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

N = int(sys.stdin.readline().strip())
nodes = []
for n in range(N): nodes.append(tuple(map(float, sys.stdin.readline().strip().split())))

edges = []
for i in range(N-1):
    for j in range(i+1, N):
        edges.append((math.sqrt((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2), i, j))
edges.sort()

parent = [i for i in range(N+1)]
total_cost = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
print(round(total_cost, 2))