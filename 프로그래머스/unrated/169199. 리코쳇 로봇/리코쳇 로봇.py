from collections import deque

def solution(board):
    
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    
    def move(x, y, i):
        while True:
            x += dx[i]; y += dy[i]
            if x < 0 or y < 0 or x >= N or y >= M:
                x -= dx[i]; y -= dy[i]
                break
            if board[x][y] == 'D':
                x -= dx[i]; y -= dy[i]
                break
        return x, y
    
    def bfs(x, y):
        queue = deque([]); queue.append((x, y, 0))
        visit = [[False] * M for n in range(N)]; visit[x][y] = True
        
        while queue:
            x, y, cnt = queue.popleft()
            if board[x][y] == 'G':
                return cnt
            for i in range(4):
                nx, ny = move(x, y, i)
                if not visit[nx][ny]:
                    if board[nx][ny] == '.' or board[nx][ny] == 'G':
                        visit[nx][ny] = True
                        queue.append((nx, ny, cnt+1))      
        return -1
    
    N = len(board)
    for n in range(N):
        board[n] = list(board[n])
    M = len(board[0])

    start_x, start_y = -1, -1
    for n in range(N):
        for m in range(M):
            if board[n][m] == 'R':
                start_x = n; start_y = m
                board[n][m] = '.'
    result = bfs(start_x, start_y)
    return result             