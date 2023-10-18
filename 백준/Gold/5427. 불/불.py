import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs_fire():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<H and 0<=ny<W:
                if board[nx][ny] != '#' and board[nx][ny] != '*':
                    board[nx][ny] = '*'
                    fire.append((nx, ny))

def bfs_sang():
    flag = False
    for _ in range(len(start)):
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<H and 0<=ny<W:
                if visit[nx][ny] == 0 and board[nx][ny] != '#' and board[nx][ny] != '*':
                    flag = True
                    visit[nx][ny] = visit[x][y]+1
                    start.append((nx, ny))
            else:
                return visit[x][y]
    if not flag: return "IMPOSSIBLE"

T = int(sys.stdin.readline())
for t in range(T):
    W, H = map(int, sys.stdin.readline().strip().split())
    board = [list(sys.stdin.readline().strip()) for h in range(H)]

    fire = deque(); start = deque()
    for h in range(H):
        for w in range(W):
            if board[h][w] == '*': fire.append((h, w))
            elif board[h][w] == '@': start.append((h, w))
    
    visit = [[0]*W for h in range(H)]; visit[start[0][0]][start[0][1]] = 1

    while True:
        bfs_fire()
        result = bfs_sang()
        if result: break
    print(result)