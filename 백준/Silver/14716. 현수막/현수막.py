import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1, 1, 1, -1, -1)
dy = (-1, 1, 0, 0, -1, 1, 1, -1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]

queue = deque([])
visit = [[False for m in range(M)] for n in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] == 1:
            cnt += 1
            queue.append((i, j)); visit[i][j] = True 
            while queue:
                x, y = queue.popleft()
                for d in range(8):
                    nx, ny = x+dx[d], y+dy[d]
                    if 0<=nx<N and 0<=ny<M:
                        if not visit[nx][ny] and board[nx][ny] == 1:
                            visit[nx][ny] = True
                            queue.append((nx, ny))
print(cnt)