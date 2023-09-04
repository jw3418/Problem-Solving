import sys

N, W = map(int, input().split())
wt = []; val = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    wt.append(tmp[0]); val.append(tmp[1])

dp = [[0 for _ in range(W+1)] for __ in range(N+1)]
for i in range(N+1):
    for weight in range(W+1):
        if i == 0 or weight == 0:
            dp[i][weight] = 0
        elif wt[i-1] <= weight:
            dp[i][weight] = max(val[i-1] + dp[i-1][weight-wt[i-1]], dp[i-1][weight])
        else:
            dp[i][weight] = dp[i-1][weight]
print(dp[N][W])