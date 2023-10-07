import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(sys.stdin.readline()[:-1]); M = int(sys.stdin.readline()[:-1])
edges = []
for m in range(M):
    a, b, c = map(int, sys.stdin.readline()[:-1].split())
    edges.append((a, b, c))
edges.sort(key=lambda x:x[2]) #weight를 기준으로 오름차순 정렬 (Kruskal)

parent = [n for n in range(N+1)]

tc = 0
for u, v, c in edges:
    if find(u) != find(v): #root노드가 같지 않다면 신장트리에 추가
        tc += c
        union(u, v)
print(tc)