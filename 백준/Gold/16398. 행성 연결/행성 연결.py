import sys
input = sys.stdin.readline

N = int(input())
adj_mat = [list(map(int, input().split())) for n in range(N)]
edges = []
for i in range(N):
    for j in range(i+1, N):
        edges.append((i, j, adj_mat[i][j]))
edges.sort(key = lambda x:x[2])


def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = [i for i in range(N)]

ans = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost
print(ans)