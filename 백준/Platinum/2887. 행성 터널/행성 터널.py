import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

N = int(input())
xlist = []; ylist = []; zlist = []
for n in range(N):
    x, y, z = map(int, input().split())
    xlist.append((x, n))
    ylist.append((y, n))
    zlist.append((z, n))
xlist.sort(); ylist.sort(); zlist.sort()

edges = []
for i in range(1, N):
    p1, a = xlist[i-1]
    p2, b = xlist[i]
    edges.append((abs(p1-p2), a, b))
    p1, a = ylist[i-1]
    p2, b = ylist[i]
    edges.append((abs(p1-p2), a, b))
    p1, a = zlist[i-1]
    p2, b = zlist[i]
    edges.append((abs(p1-p2), a, b))
edges.sort()

parent = [i for i in range(N+1)]
ans = 0
for cost, a, b in edges:
    if find(a) != find(b): #root노드가 같지 않다면 신장트리에 추가
        union(a, b)
        ans += cost
print(ans)