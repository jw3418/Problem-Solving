import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for e in range(E)]
edges.sort(key=lambda x:x[2])

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = [v for v in range(V+1)]
ans = 0
for u, v, w in edges:
    if find(u) != find(v):
        ans += w
        union(u, v)
print(ans)