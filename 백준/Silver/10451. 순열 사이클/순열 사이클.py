import sys
input = sys.stdin.readline

def dfs(cur):
    visit[cur] = True
    for nex in graph[cur]:
        if not visit[nex]:
            dfs(nex)

T = int(input())
for t in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    graph = [[] for n in range(N+1)]
    for i in range(N): graph[i+1].append(li[i])
    
    visit = [False]*(N+1)
    cnt = 0
    for n in range(1, N+1):
        if not visit[n]:
            dfs(n); cnt += 1
    print(cnt)