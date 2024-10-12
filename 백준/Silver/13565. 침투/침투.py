import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, input().split())
board = [list(map(int, list(input().strip()))) for n in range(N)]

queue = deque([])
visit = [[False]*M for n in range(N)]
for m in range(M):
    if board[0][m] == 0:
        queue.append((0, m))
        visit[0][m] = True

flag = False
while queue:
    x, y = queue.popleft()
    if x == N-1:
        flag = True
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 0 and not visit[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = True
if flag: print("YES")
else: print("NO")