import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    global ans
    visit[cur] = True
    for nex in graph[cur]:
        if not visit[nex]:
            ans+=1; dfs(nex)

N, M = map(int, input().strip().split())
graph = [[] for n in range(N)]
visit = [False for n in range(N)]
root = [True for n in range(N)] #마약원산지

for m in range(M):
    a, b = input().strip().split()
    graph[ord(a)-65].append(ord(b)-65)
    root[ord(b)-65] = False
    
delete = input().strip().split()[1:]
for n in range(len(delete)): visit[ord(delete[n])-65] = True

ans = 0
for n in range(N):
    if root[n] and not visit[n]: dfs(n)
print(ans)