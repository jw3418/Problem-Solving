import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b:
        parent[b] = a #더 작은 노드에 합침
    else:
        parent[a] = b

G = int(sys.stdin.readline()[:-1])
P = int(sys.stdin.readline()[:-1])


parent = {i: i for i in range(G+1)}

count = 0
for p in range(1, P+1):
    g = int(sys.stdin.readline()[:-1])
    g = find(g) #g의 루트 부모 노드를 찾음

    if g == 0: break # 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

    union(g, g-1)
    count += 1
print(count)