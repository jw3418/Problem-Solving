import sys
from collections import deque
input = sys.stdin.readline

dr_o = (-1, -1, 0, 0, 1, 1)
dc_o = (0, 1, -1, 1, 0, 1)
dr_e = (-1, -1, 0, 0, 1, 1)
dc_e = (-1, 0, -1, 1, -1, 0)

W, H = map(int, input().split())
tboard = [list(map(int, input().split())) for h in range(H)]
C, R = W+2, H+2
board = [[0]*C for r in range(R)]
for i in range(H):
    for j in range(W):
        board[i+1][j+1] = tboard[i][j] # masking!

visit = [[False] * C for r in range(R)]; visit[0][0] = True
queue = deque([]); queue.append((0, 0))

cnt = 0
while queue:
    r, c = queue.popleft()
    if r%2 == 0:
        for i in range(6):
            nr, nc = r+dr_e[i], c+dc_e[i]
            if 0<=nr<R and 0<=nc<C:
                if board[nr][nc] == 0:
                    if not visit[nr][nc]:
                        queue.append((nr, nc))
                        visit[nr][nc] = True
                else: cnt += 1
    else:
        for i in range(6):
            nr, nc = r+dr_o[i], c+dc_o[i]
            if 0<=nr<R and 0<=nc<C:
                if board[nr][nc] == 0:
                    if not visit[nr][nc]:
                        queue.append((nr, nc))
                        visit[nr][nc] = True
                else: cnt += 1
print(cnt)