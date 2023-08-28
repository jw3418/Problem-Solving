import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a != b: #parent랑 count 모두 a에 합쳐줌
        parent[b] = a
        count[a] += count[b]

T = int(sys.stdin.readline()[:-1])
for t in range(T):
    F = int(sys.stdin.readline()[:-1])

    parent = dict(); count = dict()
    for f in range(F):
        a, b = map(str, sys.stdin.readline()[:-1].split())

        if a not in parent:
            parent[a] = a; count[a] = 1
        if b not in parent:
            parent[b] = b; count[b] = 1

        if find(a) != find(b):
            union(a, b)

        print(count[find(a)])
