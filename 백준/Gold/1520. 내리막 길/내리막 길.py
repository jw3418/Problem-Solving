import sys

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def dfs(x, y):
    if (x, y) == (M-1, N-1):
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if board[x][y] > board[nx][ny]:
                cnt += dfs(nx, ny)
    dp[x][y] = cnt

    return dp[x][y]
    
M, N = map(int, sys.stdin.readline()[:-1].split())
board = []
for m in range(M):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

dp = [[-1] * N for _ in range(M)]
print(dfs(0, 0))
