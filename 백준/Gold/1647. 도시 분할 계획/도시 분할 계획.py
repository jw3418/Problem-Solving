import sys
from itertools import combinations

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

N, M = map(int, sys.stdin.readline()[:-1].split())
edges = []
for m in range(M):
    A, B, C = map(int, sys.stdin.readline()[:-1].split()); edges.append((A, B, C))
edges.sort(key=lambda x:x[2])

tc = 0; path = []
parent = [n for n in range(N+1)]
for i in range(M):
    u, v, c = edges[i]
    if find(u) != find(v):
        tc += c; union(u, v)
        path.append((u, v, c))
path.sort(key=lambda x:x[2])
print(tc - path[-1][2]) #MST의 total cost에서 가중치가 가장 큰 edge를 뺌