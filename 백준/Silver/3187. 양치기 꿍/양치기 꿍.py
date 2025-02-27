import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

R, C = map(int, input().split())
board = [list(input().strip()) for r in range(R)]

visit = [[False]*C for r in range(R)]
vsum = 0; ksum = 0
for i in range(R):
    for j in range(C):
        if not visit[i][j] and board[i][j] != '#':
            vset = set(); kset = set()
            visit[i][j] = True
            queue = deque([]); queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                if board[x][y] == 'v': vset.add((x, y))
                elif board[x][y] == 'k': kset.add((x, y))
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if 0<=nx<R and 0<=ny<C:
                        if not visit[nx][ny] and board[nx][ny] != '#':
                            visit[nx][ny] = True
                            queue.append((nx, ny))
            # print(vset, kset)
            if len(vset) >= len(kset): vsum += len(vset)
            else: ksum += len(kset)
print(ksum, vsum)