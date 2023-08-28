import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque([])
    x, y = src
    queue.append([x, y, 0])

    while queue:
        # 물 퍼짐
        for _ in range(len(water)):
            x, y = water.popleft()
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[nx][ny] == '.':
                        board[nx][ny] = '*'
                        water.append([nx, ny])

        visit = [[False] * C for _ in range(R)]
        for _ in range(len(queue)):
            x, y, cnt = queue.popleft()
            if x == dest[0] and y == dest[1]:
                print(cnt)
                return
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if (board[nx][ny] == '.' or board[nx][ny] == 'D') and not visit[nx][ny]:
                        queue.append([nx, ny, cnt + 1])
                        visit[nx][ny] = True
        
    print('KAKTUS')

R, C = map(int, sys.stdin.readline()[:-1].split())
board = []
dest = []; src = []; water = deque([])
for r in range(R):
    tmp = list(sys.stdin.readline()[:-1])
    for c in range(C):
        if tmp[c] == 'D':
            dest = [r, c]
        elif tmp[c] == 'S':
            src = [r, c]
        elif tmp[c] == '*':
            water.append([r, c])
    board.append(tmp)

bfs()