import sys
import math
input = sys.stdin.readline

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

T = int(input())
for t in range(T):
    N = int(input())
    li = [list(map(int, input().split())) for n in range(N)]
    parent = [i for i in range(N)]
    for i in range(N):
        x1, y1, r1 = li[i]
        for j in range(N):
            x2, y2, r2 = li[j]
            if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1+r2:
                union(i, j)
    for i in range(N): find(i)
    print(len(set(parent)))