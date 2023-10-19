import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def melt():
    while wqueue:
        x, y = wqueue.popleft()
        if board[x][y] == 'X': board[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not wvisit[nx][ny]:
                    if board[nx][ny] == 'X':
                        wvisit[nx][ny] = True
                        wqueue_tmp.append((nx, ny))
                    else:
                        wvisit[nx][ny] = True
                        wqueue.append((nx, ny))

def move():
    while squeue:
        x, y = squeue.popleft()
        if (x, y) == (d_x, d_y): return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not svisit[nx][ny]:
                    if board[nx][ny] == '.':
                        svisit[nx][ny] = True
                        squeue.append((nx, ny))
                    else:
                        svisit[nx][ny] = True
                        squeue_tmp.append((nx, ny))
    return False


R, C = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for r in range(R)]

swan = []
squeue = deque(); squeue_tmp = deque(); wqueue = deque(); wqueue_tmp = deque()
svisit = [[False]*C for r in range(R)]; wvisit = [[False]*C for r in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            wqueue.append((i, j))
            swan.append((i, j))
        elif board[i][j] == '.':
            wqueue.append((i, j))
            wvisit[i][j] = True

s_x, s_y, d_x, d_y = swan[0][0], swan[0][1], swan[1][0], swan[1][1]
squeue.append((s_x, s_y)); svisit[s_x][s_y] = True
board[s_x][s_y] = '.'; board[d_x][d_y] = '.'

answer = 0
while True:
    melt()
    if move(): break
    squeue, wqueue = squeue_tmp, wqueue_tmp
    squeue_tmp, wqueue_tmp = deque(), deque()
    answer += 1
print(answer)