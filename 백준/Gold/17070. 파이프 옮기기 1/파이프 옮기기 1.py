import sys

N = int(sys.stdin.readline()[:-1])
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)] #파이프 끝의 위치

dp[0][1][0] = 1
for i in range(2, N): # 0행 먼저 채워주기
    if board[0][i] == 0: dp[0][i][0] = dp[0][i-1][0]

for i in range(1, N):
    for j in range(1, N):
        if board[i][j] == 0: #가로, 세로 파이프 놓을 수 있는 경우
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0: #대각선 파이프 놓을 수 있는 경우
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])