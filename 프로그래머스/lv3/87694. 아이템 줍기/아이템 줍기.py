from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    
    # 좌표 개념으로 이동하기위해 크기를 두배 늘려줌
    characterX *= 2; characterY *= 2; itemX *= 2; itemY *= 2
    board = [[False] * (51*2) for _ in range(51*2)]
    
    for r in rectangle:
        # 직사각형의 테두리 및 내부 모두 True로
        for x in range(r[0]*2, r[2]*2+1):
            for y in range(r[1]*2, r[3]*2+1):
                board[x][y] = True
                
    for r in rectangle:
        # 직사각형의 테두리만 남기고 모두 False로
        for x in range(r[0]*2+1, r[2]*2):
            for y in range(r[1]*2+1, r[3]*2):
                board[x][y] = False
    
    queue = deque([]); queue.append((characterX, characterY, 0))
    visit = [[False] * (51*2) for _ in range(51*2)]; visit[characterX][characterY] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if (x, y) == (itemX, itemY):
            return cnt/2
        
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < (51*2) and 0 <= ny < (51*2):
                if not visit[nx][ny] and board[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny, cnt+1))
            