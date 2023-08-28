from collections import deque

def solution(maps):
    N = len(maps)
    for n in range(N):
        maps[n] = list(maps[n])
    M = len(maps[0])
    
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    
    def bfs(x, y):
        queue = deque([]); queue.append((x, y))
        visit[x][y] = True
        
        days = int(maps[x][y])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if not visit[nx][ny]:
                        if maps[nx][ny] != 'X':
                            visit[nx][ny] = True
                            queue.append((nx, ny))
                            days += int(maps[nx][ny])
        result.append(days)
    
    result = []
    visit = [[False] * M for n in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not visit[i][j]:
                bfs(i, j)
    if not result:
        return [-1]
    else:
        result.sort()
        return result