MOD = 1_000_000_000
N = int(input())

# dp[length][digit][mask]
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

for d in range(1, 10):
    dp[1][d][1 << d] = 1

for length in range(1, N):
    for digit in range(10):
        for mask in range(1 << 10):
            if dp[length][digit][mask] == 0:
                continue

            for next_digit in [digit - 1, digit + 1]:
                if 0 <= next_digit < 10:
                    next_mask = mask | (1 << next_digit)
                    dp[length + 1][next_digit][next_mask] += dp[length][digit][mask]
                    dp[length + 1][next_digit][next_mask] %= MOD

FULL_MASK = (1 << 10) - 1
answer = sum(dp[N][d][FULL_MASK] for d in range(10)) % MOD

print(answer)
