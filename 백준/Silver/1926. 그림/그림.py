import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]

def bfs(x, y):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visit[nx][ny] and board[nx][ny] == 1:
                    cnt += 1
                    visit[nx][ny] = True
                    queue.append((nx, ny))
    result.append(cnt)

visit = [[False]*M for n in range(N)]
result = []
for n in range(N):
    for m in range(M):
        if not visit[n][m] and board[n][m] == 1:
            bfs(n, m)
print(len(result))
if result: print(max(result))
else: print(0)