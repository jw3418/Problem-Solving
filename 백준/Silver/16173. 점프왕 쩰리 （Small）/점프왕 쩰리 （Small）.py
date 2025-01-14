import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 1)
dy = (1, 0)

N = int(input())
board = [list(map(int, input().split())) for n in range(N)]

queue = deque([]); queue.append((0, 0))
visit = [[False for n in range(N)] for n in range(N)]; visit[0][0] = True
while queue:
    x, y = queue.popleft()
    if (x, y) == (N-1, N-1):
        print("HaruHaru"); exit()
    for i in range(2):
        nx, ny = x+board[x][y]*dx[i], y+board[x][y]*dy[i]
        if 0<=nx<N and 0<=ny<N:
            if not visit[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = True
print("Hing")