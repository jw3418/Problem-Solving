import sys
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
ddx = (-1, -2, -2, -1, 1, 2, 2,1)
ddy = (-2, -1, 1, 2, 2, 1, -1, -2)

K = int(sys.stdin.readline().strip())
W, H = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for h in range(H)]

queue = deque([]); queue.append((0, 0, 0))
visit = [[[-1]*(K+1) for w in range(W)] for h in range(H)]; visit[0][0][0] = 0

while queue:
    x, y, cnt = queue.popleft()

    if (x, y) == (H-1, W-1): print(visit[x][y][cnt]); exit()

    if cnt < K:
        for i in range(8): #말처럼 이동
            nx = x + ddx[i]; ny = y +ddy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == 0 and visit[nx][ny][cnt+1] == -1:
                    visit[nx][ny][cnt+1] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt+1))

    for i in range(4): #그냥 이동
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] == 0 and visit[nx][ny][cnt] == -1:
                visit[nx][ny][cnt] = visit[x][y][cnt] + 1
                queue.append((nx, ny, cnt))
print(-1)