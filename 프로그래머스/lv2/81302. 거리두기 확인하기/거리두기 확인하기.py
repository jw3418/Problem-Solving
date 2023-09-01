from collections import deque

def solution(places):
    
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    
    def check(x, y):
        queue = deque([]); queue.append((x, y))
        visit = [[False] * 5 for _ in range(5)]; visit[x][y] = True
        
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]; ny = cy + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if abs(x - nx) + abs(y - ny) <= 2: 
                        if not visit[nx][ny]:
                            if board[nx][ny] == 'P': return False
                            elif board[nx][ny] == 'X': continue
                            else: queue.append((nx, ny)); visit[nx][ny] = True
                    
        return True
                    
    
    result = []
    for place in places:
        
        board = []
        for p in place:
            board.append(list(p))
            
        break_flag = False
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'P':
                    if not check(i, j): result.append(0); break_flag = True; break
            if break_flag: break
        
        if break_flag: continue
        else: result.append(1)
        
    return result