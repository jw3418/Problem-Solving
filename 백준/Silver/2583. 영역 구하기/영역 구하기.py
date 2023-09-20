import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline()[:-1].split())
board = [[0]*M for _ in range(N)]
for k in range(K):
    y1, x1, y2, x2 = map(int, sys.stdin.readline()[:-1].split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(x, y):
    q = deque([]); q.append((x, y))
    visit[x][y] = True; cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and board[nx][ny] == 0:
                    q.append((nx, ny)); visit[nx][ny] = True
    return cnt

visit = [[False]*M for _ in range(N)]; result = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not visit[i][j]:
            result.append(bfs(i, j))
print(len(result))
result.sort(); print(' '.join(map(str, result)))