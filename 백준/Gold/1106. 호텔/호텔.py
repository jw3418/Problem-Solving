C, N = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(N)]

dp = [float('inf')] * (C + 100)
dp[0] = 0

for cost, people in costs:
    for i in range(people, C + 100):
        dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[C:]))
