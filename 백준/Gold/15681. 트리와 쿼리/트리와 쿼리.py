import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = [[] for n in range(N+1)]
for n in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur):
    visit[cur] += 1
    for nex in graph[cur]:
        if visit[nex] == 0:
            visit[cur] += dfs(nex)
    return visit[cur]

visit = [0] * (N+1)
dfs(R)
for q in range(Q): print(visit[int(input())])