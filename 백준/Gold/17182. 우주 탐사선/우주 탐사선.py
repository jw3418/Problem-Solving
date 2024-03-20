import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
adj_mat = [list(map(int, input().split())) for n in range(N)]

for k in range(N): # 거쳐가는 노드
    for i in range(N): # 출발 노드
        for j in range(N): # 도착 노드
            adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k]+adj_mat[k][j])

def dfs(cur, cnt, dist):
    global result
    if cnt == N:
        result = min(result, dist)
        return
    for nex in range(N):
        if not visit[nex]:
            visit[nex] = True
            dfs(nex, cnt+1, dist+adj_mat[cur][nex])
            visit[nex] = False

visit = [False]*N
visit[K] = True
result = int(10e9)
dfs(K, 1, 0)
print(result)