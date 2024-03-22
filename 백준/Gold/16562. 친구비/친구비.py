import sys
from collections import deque

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if pay[a] < pay[b]: parent[b] = a
    else: parent[a] = b

N, M, K = map(int, input().split())
pay = [0]; pay.extend(list(map(int, input().split())))

parent = [n for n in range(N+1)]
for m in range(M):
    v, w = map(int, input().split())
    if find(v) != find(w): union(v, w)

for n in range(N+1): find(n)

parent = list(set(parent[1:]))
need = 0
for i in range(len(parent)): need += pay[parent[i]]

if need <= K: print(need)
else: print("Oh no")