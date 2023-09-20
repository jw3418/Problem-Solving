import sys
from collections import deque

N = int(sys.stdin.readline()[:-1])

board = []; max_height = 0; min_height = int(10e9)
for n in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    max_height = max(max_height, max(tmp))
    min_height = min(min_height, min(tmp))
    board.append(tmp)

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(x, y):
    q = deque([]); q.append((x, y))
    check[x][y] = False

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if check[nx][ny]:
                    q.append((nx, ny)); check[nx][ny] = False

answer = 1
for h in range(min_height, max_height):
    check = [[True]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] <= h: check[i][j] = False

    count = 0
    for i in range(N):
        for j in range(N):
            if check[i][j]: count += 1; bfs(i, j)
    answer = max(answer, count)
print(answer)