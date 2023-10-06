import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dx = (0, 1, 1)
dy = (1, 0, 1)

board = [list(map(int, input()[:-1].split())) for n in range(N)]
dp = [[0 for m in range(M+1)] for n in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + board[i-1][j-1]

print(dp[N][M])