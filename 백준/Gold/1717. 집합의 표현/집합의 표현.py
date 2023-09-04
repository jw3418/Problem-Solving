import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, sys.stdin.readline()[:-1].split())
parent = [i for i in range(N+1)]
for m in range(M):
    cmd, a, b = map(int, sys.stdin.readline()[:-1].split())
    if cmd == 0:
        union(parent, a, b)
    elif cmd == 1:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
