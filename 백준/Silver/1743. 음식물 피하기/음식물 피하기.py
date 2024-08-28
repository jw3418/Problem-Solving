import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M, K = map(int, input().split())
board = [[0]*M for n in range(N)]
for k in range(K):
    x, y = map(int, input().split()); x-=1; y-=1
    board[x][y] = 1

def bfs(x, y):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

visit = [[False]*M for n in range(N)]; max_ = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visit[i][j]:
            max_ = max(max_, bfs(i, j))
print(max_)