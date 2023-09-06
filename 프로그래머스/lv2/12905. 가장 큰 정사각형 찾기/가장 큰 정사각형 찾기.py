def solution(board):
    N = len(board); M = len(board[0])
    
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1 #현재 위치에서, (상, 좌상, 좌)를 확인해보면 됨
            
    max_width = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            max_width = max(max_width, dp[i][j])
    return max_width**2