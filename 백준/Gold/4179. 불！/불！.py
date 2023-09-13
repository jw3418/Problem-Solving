import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

R, C = map(int, sys.stdin.readline()[:-1].split())

board = []; queue_f = deque([]); queue_j = deque([]); ex = set()
visit_f = [[-1]*C for r in range(R)]; visit_j = [[-1]*C for r in range(R)]
for r in range(R):
    tmp = list(sys.stdin.readline()[:-1])
    for c in range(C):
        if tmp[c] == 'J': queue_j.append((r, c)); visit_j[r][c] = 0
        elif tmp[c] == 'F': queue_f.append((r, c)); visit_f[r][c] = 0
        elif tmp[c] == '.' and (c == 0 or c == C-1 or r == 0 or r == R-1): ex.add((r, c))
    board.append(tmp)

tmp = list(queue_j)
for t in tmp:
    if t[0] == 0 or t[0] == R-1 or t[1] == 0 or t[1] == C-1: print(1); exit() #즉시 탈출할 수 있는 경우

while queue_f: #visit_f 완성
    x, y = queue_f.popleft()

    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if visit_f[nx][ny] == -1 and board[nx][ny] != '#':
                visit_f[nx][ny] = visit_f[x][y] + 1
                queue_f.append((nx, ny))

while queue_j: #지훈이 탈출 bfs
    x, y = queue_j.popleft()
    if (x, y) in ex:
        print(visit_j[x][y]+1); exit()
    
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if visit_j[nx][ny] == -1 and board[nx][ny] == '.':
                if visit_f[nx][ny] == -1 or visit_f[nx][ny] > visit_j[x][y]+1:
                    visit_j[nx][ny] = visit_j[x][y] + 1
                    queue_j.append((nx, ny))

print("IMPOSSIBLE")