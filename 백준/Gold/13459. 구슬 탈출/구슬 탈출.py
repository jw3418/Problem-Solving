import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O': #보드를 기울여서 움직여야함
        x += dx; y += dy; cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by, depth):
    queue = deque([])
    queue.append([rx, ry, bx, by, depth]); visit.append((rx, ry, bx, by))
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(1)
                    return
                if nrx == nbx and nry == nby: #cnt가 작은 색깔의 구슬이 해당 자리에 있는 게 맞음
                    if rcnt > bcnt:
                        nrx -= dx[i]; nry -= dy[i]
                    else:
                        nbx -= dx[i]; nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visit:
                    queue.append([nrx, nry, nbx, nby, depth+1])
                    visit.append((nrx, nry, nbx, nby))
    print(0)

N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(sys.stdin.readline()[:-1]))
    for m in range(M):
        if board[n][m] == 'R':
            rx, ry = n, m
        elif board[n][m] == 'B':
            bx, by = n, m

visit = []
bfs(rx, ry, bx, by, 1)