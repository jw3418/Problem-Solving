import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for n in range(1, N+1): graph[n].sort()

def dfs(cur):
    global cnt
    result[cur] = cnt; cnt += 1

    for nex in graph[cur]:
        if not visit[nex]:
            visit[nex] = True
            dfs(nex)

visit = [False] * (N+1); visit[R] = True
result = [0] * (N+1); cnt = 1
dfs(R)
result = result[1:]
for n in range(N): print(result[n])