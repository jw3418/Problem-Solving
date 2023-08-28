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

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

parent = [i for i in range(N+1)]
for n in range(1, N+1):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, N+1):
        if tmp[i-1] == 1:
            union(n, i)

plan = list(map(int, sys.stdin.readline().strip().split()))
flag = find(plan[0])
for p in plan[1:]:
    if find(p) != flag:
        print("NO"); exit()
print("YES")