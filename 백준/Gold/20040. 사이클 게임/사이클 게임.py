import sys
# sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [n for n in range(N)]
rank = [0 for n in range(N)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

for m in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(m+1)
        break
    union(a, b)
else: print(0)