import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, input().split())
board = []
for m in range(M): board.append(list(input().strip()))

def bfs(x, y, flag):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if not visit[nx][ny] and board[nx][ny] == flag:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt


visit = [[False]*N for m in range(M)]
B = 0; W = 0
for x in range(M):
    for y in range(N):
        if not visit[x][y]:
            if board[x][y] == 'B':
                B += bfs(x, y, 'B')**2
            else:
                W += bfs(x, y, 'W')**2
print(W, B)