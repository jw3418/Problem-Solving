import sys

N, K = map(int, sys.stdin.readline()[:-1].split())
coin = []
for n in range(N):
    coin.append(int(sys.stdin.readline()[:-1]))

dp = [0 for _ in range(K+1)] #dp[j]는 가치의 합이 j가 되는 경우의 수

dp[0] = 1
for i in range(N): #i는 coin의 index
    for j in range(coin[i], K+1): #j는 가치의 합, dp[j]는 가치의 합이 j가 되는 경우의 수
        dp[j] += dp[j - coin[i]]

print(dp[K])