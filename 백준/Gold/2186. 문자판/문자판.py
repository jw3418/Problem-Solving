import sys
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y, idx):
    if dp[x][y][idx] != -1: return dp[x][y][idx]
    if idx == len(target)-1: return 1

    local_answer = 0
    for i in range(4):
        for k in range(1, K+1):
            nx, ny = x+k*dx[i], y+k*dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == target[idx+1]:
                    local_answer += dfs(nx, ny, idx+1)
    dp[x][y][idx] = local_answer
    return local_answer

N, M, K = map(int, input().strip().split())
board = []
for n in range(N): board.append(list(input().strip()))
target = list(input().strip())

dp = [[[-1 for _ in range(len(target))] for m in range(M)] for n in range(N)] #3차원 dp table

answer = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == target[0]:
            answer += dfs(n, m, 0)
print(answer)