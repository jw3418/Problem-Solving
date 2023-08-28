import sys
sys.setrecursionlimit(10**6)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] > board[x][y]:
                cnt = max(cnt, dfs(nx, ny))
    
    dp[x][y] = cnt + 1 #현재 칸도 포함
    return dp[x][y]


N = int(sys.stdin.readline()[:-1])
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

dp = [[-1] * N for _ in range(N)]
max_cnt = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            max_cnt = max(max_cnt, dfs(i, j))
print(max_cnt)