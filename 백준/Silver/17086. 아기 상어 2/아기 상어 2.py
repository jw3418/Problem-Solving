import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1, -1, 1, 1, -1)
dy = (-1, 1, 0, 0, 1, 1, -1, -1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]

queue = deque([])
visit = [[-1]*M for n in range(N)]
for n in range(N):
    for m in range(M):
        if board[n][m] == 1:
            queue.append((n, m))
            visit[n][m] = 0

while queue:
    x, y = queue.popleft()
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 0 and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y]+1
                queue.append((nx, ny))
ans = 0
for n in range(N): ans = max(ans, max(visit[n]))
print(ans)