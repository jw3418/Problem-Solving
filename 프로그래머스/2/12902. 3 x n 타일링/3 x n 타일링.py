def solution(N):
    if N%2 != 0: return 0

    dp = [0 for _ in range(N+1)]
    dp[0] = 1; dp[2] = 3
    
    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2
        dp[i] %= 1000000007
    return dp[N]