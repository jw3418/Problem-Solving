from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def solution(board):
    N = len(board)
    
    queue = deque([]); queue.append((0, 0, 0, 1)); queue.append((0, 0, 0, 3))
    dp = [[[10000]*N for n in range(N)] for d in range(4)] #방향마다 dp table을 나눔 [direction][x][y]
    
    while queue:
        x, y, cost, pre_dir = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                ncost = cost + 1
                if pre_dir != i: ncost += 5
                if ncost < dp[i][nx][ny]:
                    dp[i][nx][ny] = ncost
                    if (nx, ny) == (N-1, N-1): continue
                    queue.append((nx, ny, ncost, i))
    
    answer = 10000
    for i in range(4): answer = min(answer, dp[i][N-1][N-1])    
    return answer*100