import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0 for _ in range(M+1)]

    dp[0] = 1
    for i in range(N): #i는 coin의 index
        for j in range(coin[i], M+1):
            dp[j] += dp[j - coin[i]]

    print(dp[M])