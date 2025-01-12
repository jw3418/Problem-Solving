import sys
from collections import deque
input = sys.stdin.readline

#동남서북
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]
sx, sy, sd = map(int, input().split()); sx-=1; sy-=1; sd-=1
ex, ey, ed = map(int, input().split()); ex-=1; ey-=1; ed-=1
if sd == 1: sd = 2
elif sd == 2: sd = 1
if ed == 1: ed = 2
elif ed == 2: ed = 1

queue = deque([]); queue.append((sx, sy, sd, 0))
visit = [[[False for _ in range(4)] for m in range(M)] for n in range(N)]; visit[sx][sy][sd] = True

while queue:
    x, y, d, cnt = queue.popleft()
    '''
    1) 현재 설정된 방향에서 1 이동
    2) 현재 설정된 방향에서 2 이동
    3) 현재 설정된 방향에서 3 이동
    4) 시계방향 90도 회전
    5) 반시계방향 90도 회전
    '''
    if (x, y, d) == (ex, ey, ed):
        print(cnt); break

    for k in range(1, 3+1):
        nx, ny = x+k*dx[d], y+k*dy[d]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 1: break
            if not visit[nx][ny][d]:
                visit[nx][ny][d] = True
                queue.append((nx, ny, d, cnt+1))
    nd = (d+1) % 4
    if not visit[x][y][nd]:
        visit[x][y][nd] = True
        queue.append((x, y, nd, cnt+1))
    nd = (d-1) % 4
    if not visit[x][y][nd]:
        visit[x][y][nd] = True
        queue.append((x, y, nd, cnt+1))
