import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N = int(input().strip())
board = []
for n in range(N): board.append(list(map(int, list(input().strip()))))

queue = deque([]); queue.append((0, 0))
visit = [[-1]*N for n in range(N)]; visit[0][0] = 0
while queue:
    x, y = queue.popleft()
    if (x, y) == (N-1, N-1): print(visit[x][y]); break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and visit[nx][ny]==-1:
            if board[nx][ny] == 1: #흰방인 경우
                queue.appendleft((nx, ny)) #흰방을 먼저 탐색하도록함
                visit[nx][ny] = visit[x][y]
            else: #검은방인 경우
                queue.append((nx, ny))
                visit[nx][ny] = visit[x][y]+1