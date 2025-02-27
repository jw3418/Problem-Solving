import sys
input = sys.stdin.readline

N, M = map(int, input().split())
school = [-1]; school.extend(list(input().split()))

edges = []
for m in range(M):
    u, v, d = map(int, input().split())
    edges.append((u, v, d))
edges.sort(key=lambda x:x[2])

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = [i for i in range(N+1)]
len_ = 0; cnt = 0
for u, v, d in edges:
    if school[u] != school[v]:
        if find(u) != find(v):
            union(u, v)
            len_ += d; cnt += 1
    if cnt == N-1: break
if cnt == N-1: print(len_)
else: print(-1)