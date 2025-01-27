import sys

def dfs(cur):
    global visit, g_cnt
    g_cnt += 1

    if cur in graph:
        for nex in graph[cur]:
            if not visit[nex]:
                visit[nex] = True
                dfs(nex)

def rdfs(cur):
    global rvisit, g_rcnt
    g_rcnt += 1

    if cur in rgraph:
        for nex in rgraph[cur]:
            if not rvisit[nex]:
                rvisit[nex] = True
                rdfs(nex)

N, M = map(int, input().split())
graph = dict(); rgraph = dict()
for m in range(M):
    a, b = map(int, input().split())
    if a in graph: graph[a].append(b)
    else: graph[a] = [b]
    if b in rgraph: rgraph[b].append(a)
    else: rgraph[b] = [a]

ans = 0
for n in range(1, N+1):
    visit = [False] * (N+1); rvisit = [False] * (N+1)
    g_cnt = -1; g_rcnt = -1
    if n in graph: dfs(n)
    if n in rgraph: rdfs(n)
    # print(visit); print(rvisit); print(g_cnt); print(g_rcnt); print()
    if g_cnt > N//2 or g_rcnt > N//2: ans += 1
print(ans)