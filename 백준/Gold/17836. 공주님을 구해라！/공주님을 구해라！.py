import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs1(x, y):
    queue = deque([]); queue.append((x, y, 0))
    visit[x][y] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == (N-1, M-1): return cnt

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] != 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny, cnt+1))
    return -1

def bfs2(x, y):
    global cx, cy
    queue = deque([]); queue.append((x, y, 0))
    visit[x][y] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        if board[x][y] == 2: cx, cy = x, y; return cnt

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] != 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny, cnt+1))
    return -1

N, M, T = map(int, input().split())
board = [list(map(int, input().strip().split())) for n in range(N)]

visit = [[False]*M for n in range(N)]
one = bfs1(0, 0)
if one == -1: one = int(10e9)

cx, cy = -1, -1
visit = [[False]*M for n in range(N)]
two = bfs2(0, 0)
if two == -1: two = int(10e9)
else:
    two += (N-1-cx)+(M-1-cy)

answer = min(one, two)
if answer == int(10e9) or answer > T: print("Fail")
else: print(answer)