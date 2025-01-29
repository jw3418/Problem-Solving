import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

N, M = map(int, input().split())
sboard = [list(map(int, input().split())) for n in range(N)]
eboard = [list(map(int, input().split())) for n in range(N)]

x, y, num = -1, -1, -1
for i in range(N):
    for j in range(M):
        if sboard[i][j] != eboard[i][j]:
            x, y, num = i, j, eboard[i][j]
            break

queue = deque([]); queue.append((x, y))
visit = [[False] * M for n in range(N)]; visit[x][y] = True
flag = sboard[x][y]
while queue:
    x, y = queue.popleft()
    if num != -1: sboard[x][y] = num
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if not visit[nx][ny] and sboard[nx][ny] == flag:
                visit[nx][ny] = True
                queue.append((nx, ny))

for i in range(N):
    for j in range(M):
        if sboard[i][j] != eboard[i][j]:
            print("NO"); exit()
print("YES")