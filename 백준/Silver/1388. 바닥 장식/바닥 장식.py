import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for n in range(N)]
visit = [[False]*M for n in range(N)]

def bfs(x, y, flag):
    dx = tuple(); dy = tuple()
    if flag == '-':
        dx = (0, 0); dy = (-1, 1)
    elif flag == '|':
        dx = (-1, 1); dy = (0, 0)
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visit[nx][ny] and board[nx][ny] == flag:
                    visit[nx][ny] = True
                    queue.append((nx, ny))

cnt = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            cnt += 1
            bfs(i, j, board[i][j])
print(cnt)