import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

R, C = map(int, input().split())
board = []
for r in range(R): board.append(list(input().strip()))

def search(x, y):
    global vmi, omi
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True

    v, o = 0, 0
    while queue:
        x, y = queue.popleft()
        if board[x][y] == 'v': v+=1
        elif board[x][y] == 'o': o+=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not visit[nx][ny] and board[nx][ny] != '#':
                    visit[nx][ny] = True
                    queue.append((nx, ny))
    if v >= o: omi += o
    else: vmi += v


visit = [[False]*C for r in range(R)]
vmi, omi = 0, 0 # 총 늑대 및 양의 개수에서 뺄 값
for i in range(R):
    for j in range(C):
        if not visit[i][j] and (board[i][j] == 'v' or board[i][j] == 'o'):
            search(i, j)

tv, to = 0, 0 # 총 늑대 및 양의 개수
for i in range(R):
    for j in range(C):
        if board[i][j] == 'v': tv+=1
        elif board[i][j] == 'o': to+=1
print(to-omi, tv-vmi)