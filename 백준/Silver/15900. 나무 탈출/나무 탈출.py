import sys
sys.setrecursionlimit(10**5*6)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split()); a -= 1; b -= 1
    edges[a].append(b)
    edges[b].append(a)

def dfs(cur, depth):
    if cur == N: return
    dists[cur] = max(dists[cur], depth)

    for nex in edges[cur]:
        if not visit[nex]:
            visit[nex] = True
            dfs(nex, depth+1)
            visit[nex] = False


dists = [0] * N
visit = [False] * N; visit[0] = True
dfs(0, 0)

sum_ = 0
for i in range(1, N):
    if len(edges[i]) == 1:
        sum_ += dists[i]

if sum_ % 2 == 0: print("No")
else: print("Yes")