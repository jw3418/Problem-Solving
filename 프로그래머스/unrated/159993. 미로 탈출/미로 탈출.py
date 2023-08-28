from collections import deque

def solution(maps):
    
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    
    N = len(maps); M = len(maps[0])
    
    def bfs(sx, sy, ex, ey):
        queue = deque([]); queue.append((sx, sy))
        visit = [[-1 for m in range(M)] for n in range(N)]; visit[sx][sy] += 1
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if maps[nx][ny] == 'X' or visit[nx][ny] != -1: continue
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
        return visit[ex][ey]
            
            
    start = tuple(); end = tuple(); lever = tuple()
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S': start = (i, j)
            elif maps[i][j] == 'E': end = (i, j)
            elif maps[i][j] == 'L': lever = (i, j)
                
    pre_count = bfs(start[0], start[1], lever[0], lever[1])
    if pre_count == -1: return -1
    post_count = bfs(lever[0], lever[1], end[0], end[1])
    if post_count == -1: return -1
    return pre_count + post_count