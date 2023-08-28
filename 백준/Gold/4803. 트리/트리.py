import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = 0
while True:
    N, M = map(int, sys.stdin.readline()[:-1].split())
    T += 1
    if N == 0 and M == 0: break

    edges = []
    for m in range(M):
        edges.append(list(map(int, sys.stdin.readline()[:-1].split())))

    parent = [i for i in range(N+1)]; cycle = set()
    for edge in edges:
        a, b = edge
        if find(a) != find(b):
            union(a, b)
        else: #cycle 발생
            cycle.add(b)
    
    for i in range(N+1): #parent 한번 갱신
        find(i)

    cycle_group = set()
    for c in cycle:
        cycle_group.add(parent[c])

    parent = set(parent[1:])
    count = 0
    for p in parent:
        if p not in cycle_group:
            count += 1
            cycle_group.add(p)

    print("Case " + str(T) + ": ", end="")
    if count == 0: print("No trees.")
    elif count == 1: print("There is one tree.")
    elif count > 1: print("A forest of " + str(count) + " trees.")