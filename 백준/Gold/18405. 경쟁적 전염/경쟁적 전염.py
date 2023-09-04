import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def infection():
    queue = []
    for x in range(N):
        for y in range(N):
            if board[x][y] != 0:
                queue.append((board[x][y], 0, x, y))
    queue.sort(); queue = deque(queue)

    while queue:
        k, s, x, y = queue.popleft()
        if s == S:
            break
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0:
                    board[nx][ny] = k
                    queue.append((k, s+1, nx, ny))


N, K = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))
S, X, Y = map(int, sys.stdin.readline()[:-1].split()); X -= 1; Y -= 1

infection()

print(board[X][Y])