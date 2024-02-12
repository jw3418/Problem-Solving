import sys
from collections import deque

dz = (1, -1, 0, 0, 0, 0)
dx = (0, 0, 1, -1, 0, 0)
dy = (0, 0, 0, 0, 1, -1)

while True:
    L, R, C = map(int, sys.stdin.readline().strip().split())
    if L==0 and R==0 and C==0: break

    board = []
    for l in range(L): board.append([list(sys.stdin.readline().strip()) for r in range(R)]); non_=sys.stdin.readline()

    S, E = -1, -1
    visit = [[[False]*C for r in range(R)] for l in range(L)]
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if board[l][r][c] == 'S': S = (l, r, c, 0)
                elif board[l][r][c] == 'E': E = (l, r, c)

    queue = deque([]); flag = False
    queue.append(S); visit[S[0]][S[1]][S[2]] = True
    while queue:
        z, x, y, cnt = queue.popleft()
        if (z, x, y) == E:
            print("Escaped in " + str(cnt) + " minute(s).")
            flag = True; break
        
        ncnt = cnt+1
        for i in range(6):
            nz=z+dz[i]; nx=x+dx[i]; ny=y+dy[i]
            if 0<=nz<L and 0<=nx<R and 0<=ny<C and not visit[nz][nx][ny]:
                if board[nz][nx][ny] == '.' or board[nz][nx][ny] == 'E':
                    queue.append((nz, nx, ny, ncnt))
                    visit[nz][nx][ny] = True
    
    if not flag: print("Trapped!")