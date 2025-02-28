import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]

coor = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2: coor.append((i, j))

def Do(g_start, r_start):
    queue = deque([]); visit = [[0]*M for n in range(N)]
    for i, j in g_start: queue.append((i, j, 1)); visit[i][j] = 1
    for i, j in r_start: queue.append((i, j, -1)); visit[i][j] = -1

    fcnt = 0
    while queue:
        x, y, step = queue.popleft()
        if visit[x][y] == 'X': continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] != 0:
                if visit[nx][ny] == 0:
                    if step < 0: queue.append((nx, ny, step-1)); visit[nx][ny] = step-1
                    else: queue.append((nx, ny, step+1)); visit[nx][ny] = step+1
                elif visit[nx][ny] != 'X':
                    if step < 0:
                        if visit[nx][ny] > 0 and abs(visit[nx][ny]) == abs(step)+1:
                            fcnt += 1; visit[nx][ny] = 'X'
                    else:
                        if visit[nx][ny] < 0 and abs(visit[nx][ny]) == abs(step)+1:
                            fcnt += 1; visit[nx][ny] = 'X'

    return fcnt
    

global_max = 0
for g_start in combinations(coor, G):
    g_start = list(g_start)
    for r_start in combinations(list(set(coor) - set(g_start)), R):
        r_start = list(r_start)
        global_max = max(global_max, Do(g_start, r_start))
print(global_max)