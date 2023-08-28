import sys
import copy

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

def dfs(sx, sy, local_total_ate, board):
    global total_ate

    ##### 상어가 (sx, sy)에 있는 물고기를 먹음
    local_total_ate += board[sx][sy][0]
    total_ate = max(local_total_ate, total_ate)
    board[sx][sy][0] = 0
    sd = board[sx][sy][1]

    ##### 물고기 이동
    for fish in range(1, 17):
        fx = -1; fy = -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == fish:
                    fx = i; fy = j; break
        if fx == -1 and fy == -1: continue
        fd = board[fx][fy][1]
        for i in range(8):
            nfd = (fd + i) % 8
            nfx = fx + dx[nfd]; nfy = fy + dy[nfd]
            if 0 <= nfx < 4 and 0 <= nfy < 4 and (nfx != sx or nfy != sy):
                board[fx][fy][1] = nfd
                board[fx][fy], board[nfx][nfy] = board[nfx][nfy], board[fx][fy]
                break

    ##### 상어 이동
    x = sx; y = sy
    for i in range(3):
        x += dx[sd]; y += dy[sd]
        if 0 <= x < 4 and 0 <= y < 4 and board[x][y][0] != 0:
            dfs(x, y, local_total_ate, copy.deepcopy(board))


board = [[0] * 4 for _ in range(4)]
for n in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, sys.stdin.readline()[:-1].split()); b1 -= 1; b2 -= 1; b3 -= 1; b4 -= 1
    board[n][0] = [a1, b1]; board[n][1] = [a2, b2]; board[n][2] = [a3, b3]; board[n][3] = [a4, b4]

total_ate = 0
dfs(0, 0, 0, board)
print(total_ate)