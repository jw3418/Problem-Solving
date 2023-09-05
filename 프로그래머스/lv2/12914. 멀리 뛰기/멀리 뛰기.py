def solution(n):
    
    if n == 1:
        return 1 % 1234567
    elif n == 2:
        return 2 % 1234567
    
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        
    return dp[n]