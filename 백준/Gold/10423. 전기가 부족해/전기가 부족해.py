import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
P = list(map(int, input().split())); P_set = set(P)
edges = [list(map(int, input().split())) for m in range(M)]
edges.sort(key=lambda x:x[2])

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a == b: return False
    if a in P_set and b in P_set: return False
    if a in P_set: parent[b] = a
    elif b in P_set: parent[a] = b
    else:
        if a < b: parent[b] = a
        else: parent[a] = b
    return True

parent = [n for n in range(N+1)]
ans = 0
for u, v, w in edges:
    if union(u, v):
        ans += w
print(ans)