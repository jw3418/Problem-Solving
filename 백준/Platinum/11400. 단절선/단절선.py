import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = dict()
for e in range(E):
    A, B = map(int, input().split())
    if A in graph: graph[A].append(B)
    else: graph[A] = [B]
    if B in graph: graph[B].append(A)
    else: graph[B] = [A]

def dfs(cur, cnt, parent):
    visit[cur] = True
    order[cur] = cnt
    lsv = order[cur]

    for nex in graph[cur]:
        if nex == parent:
            continue
        if visit[nex] == True:
            lsv = min(lsv, order[nex])
            continue
        
        sub_lsv = dfs(nex, cnt+1, cur)
        lsv = min(sub_lsv, lsv)

        if sub_lsv > order[cur]:
            result.add(tuple(sorted([cur, nex])))
    
    return lsv


visit = [False] * (V+1)
order = [-1] * (V+1)
result = set()
dfs(1, 1, -1)

result = sorted(result, key=lambda x:(x[0], x[1]))
print(len(result))
for x, y in result: print(x, y)