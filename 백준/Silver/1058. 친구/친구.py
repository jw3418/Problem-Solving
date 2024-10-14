import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj = [[0]*N for n in range(N)]
for i in range(N):
    tmp = list(input().strip())
    for j in range(N):
        if tmp[j] == 'Y': adj[i][j] = 1

def bfs(n):
    queue = deque([]); queue.append((n, 0))
    visit = [False]*N; visit[n] = True
    Cnt = 0
    while queue:
        cur, cnt = queue.popleft()
        if cnt >= 2: continue
        for nex in range(N):
            if not visit[nex] and adj[cur][nex]:
                queue.append((nex, cnt+1))
                visit[nex] = True
                Cnt += 1
    return Cnt

res = 0
for n in range(N):
    res = max(res, bfs(n))
print(res)