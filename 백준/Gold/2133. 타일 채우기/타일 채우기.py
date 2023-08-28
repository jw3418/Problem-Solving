import sys

N = int(input())

dp = [0 for _ in range(N + 1)]

if N > 1:
    dp[2] = 3

    for i in range(4, N+1):
        if i % 2 == 0:
            tmp = dp[i-2] * dp[2]
            tmp += 2
            for j in range(2, i-4+1, 2):
                tmp += dp[j] * 2
            dp[i] = tmp
        else:
            continue
    print(dp[N])
else:
    print(0)