import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

M, N = map(int, input().split())
board = []
for m in range(M): board.append(list(map(int, input().split())))

def dfs(x, y):
    if (x, y) == (M-1, N-1):
        return 1
    elif dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            if board[x][y] > board[nx][ny]:
                cnt += dfs(nx, ny)
    dp[x][y] = cnt
    return dp[x][y]

dp = [[-1]*N for m in range(M)]
dfs(0, 0)
print(dp[0][0])