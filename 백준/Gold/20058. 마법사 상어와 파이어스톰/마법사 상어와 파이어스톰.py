import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True
    local_max_space = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < 2**N and 0 <= ny < 2**N:
                if board[nx][ny] != 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    local_max_space += 1
    
    return local_max_space


N, Q = map(int, sys.stdin.readline()[:-1].split())
board = [] # 각 칸 별 얼음의 양
for n in range(2**N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))
L = list(map(int, sys.stdin.readline()[:-1].split())) # Q번의 단계

for q in range(Q): #단계 수행
    step = 2**L[q]

    for i in range(0, 2**N, step): #회전
        row = board[i:i+step]; semi_boards = []
        for j in range(0, 2**N, step):
            col = []
            for s in range(step):
                col.append(row[s][j:j+step])
            col = reversed(col)
            semi_board= list(map(list, zip(*col)))
            for x in range(step):
                for y in range(step):
                    board[i+x][j+y] = semi_board[x][y]
    
    ice = [[0] * 2**N for _ in range(2**N)]
    for x in range(2**N):
        for y in range(2**N):
            if board[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]; ny = y + dy[i]
                    if 0 <= nx < 2**N and 0 <= ny < 2**N:
                        if board[nx][ny] > 0: cnt += 1
                if cnt < 3:
                    ice[x][y] = board[x][y] - 1
                else:
                    ice[x][y] = board[x][y]
    board = ice.copy()

total = 0; max_space = 0
visit = [[False] * 2**N for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        total += board[i][j]
        if board[i][j] != 0 and not visit[i][j]:
            max_space = max(max_space, bfs(i, j))

print(total)
print(max_space)