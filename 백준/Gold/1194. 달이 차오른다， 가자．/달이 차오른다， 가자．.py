import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def haveKey(key, door):
    result = key & (1 << (ord(door) - ord('A')))
    if result: return True
    else: return False

def bfs(x, y):
    global min_cnt

    queue = deque([]); queue.append((x, y, 0, 0))
    visit = [[[False] * (1 << 6) for m in range(M)] for n in range(N)]; visit[x][y][0] = True #6개의 key -> 6개의 bits
    board[x][y] = '.'

    while queue:
        x, y, cnt, key = queue.popleft()
        if board[x][y] == '1':
            min_cnt = min(min_cnt, cnt); return
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny][key]:
                    if board[nx][ny] == '.' or board[nx][ny] == '1': #빈 공간 또는 출구
                        visit[nx][ny][key] = True
                        queue.append((nx, ny, cnt+1, key))

                    elif 97 <= ord(board[nx][ny]) <= 122: #열쇠
                        nkey = key | (1 << (ord(board[nx][ny]) - ord('a')))
                        visit[nx][ny][nkey] = True
                        queue.append((nx, ny, cnt+1, nkey))

                    elif 65 <= ord(board[nx][ny]) <= 90: #문
                        if haveKey(key, board[nx][ny]):
                            visit[nx][ny][key] = True
                            queue.append((nx, ny, cnt+1, key))
    return


N, M = map(int, sys.stdin.readline()[:-1].split())

board = deque([]); start_x = -1; start_y = -1
for n in range(N):
    tmp = list(sys.stdin.readline()[:-1])
    for m in range(M):
        if tmp[m] == '0': start_x = n; start_y = m
    board.append(tmp)

min_cnt = int(10e9)
bfs(start_x, start_y)
if min_cnt == int(10e9): print(-1)
else: print(min_cnt)