import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur):
    global cnt
    cnt += 1
    graph[cur].sort(reverse=True)
    for nex in graph[cur]:
        if not visit[nex]:
            result[nex] = cnt
            visit[nex] = True
            dfs(nex)

result = [0]*(N+1)
result[R] = 1
visit = [False]*(N+1)
visit[R] = True
cnt = 1
dfs(R)
for i in range(1, N+1): print(result[i])