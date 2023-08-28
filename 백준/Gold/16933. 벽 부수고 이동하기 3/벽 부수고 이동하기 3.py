import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M, K = map(int, sys.stdin.readline()[:-1].split())
board = [list(map(int, sys.stdin.readline()[:-1].strip())) for _ in range(N)]
MAX = float('inf')
visit = [[[MAX] * (K+1) for _ in range(M)] for _ in range(N)]

result = MAX
queue = deque([(0, 0, 1, K)])
visit[0][0][K] = 0

while queue:
    x, y, turn, wall = queue.popleft()
    if (x, y) == (N-1, M-1):
        result = min(result, turn)
        continue
    
    day = turn % 2
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0 and visit[nx][ny][wall] > turn: #벽 부수지 않고 이동
                visit[nx][ny][wall] = turn
                queue.append((nx, ny, turn+1, wall))
            elif board[nx][ny] == 1 and wall and visit[nx][ny][wall-1] > turn:
                if day: #벽 부수고 이동
                    visit[nx][ny][wall-1] = turn
                    queue.append((nx, ny, turn+1, wall-1))
                else: #밤이어서 벽을 부술 수 없는 경우 (낮이 되면 부술 수 있음)
                    queue.append((x, y, turn+1, wall))

print(result if result < MAX else -1)