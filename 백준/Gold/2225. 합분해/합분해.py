import sys

tmp = list(map(int, sys.stdin.readline()[:-1].split(' ')))
N = tmp[0] - 1; K = tmp[1] - 1


dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if i == 0:
            dp[i][j] = j + 1
        if j == 0:
            dp[i][j] = 1
        else:
            continue

for i in range(1, N+1):
    for j in range(1, K+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[N][K] % 1000000000)