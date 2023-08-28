import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(x, y): #얼음의 좌표와 좌표 당 녹는 양을 반환
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True
    ice = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    ice.append((nx, ny))
    return ice

def ice_remove(ice):
    sub = []
    for x, y in ice:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    cnt += 1
        sub.append(cnt)

    idx = 0
    for x, y in ice:
        board[x][y] -= sub[idx]; idx += 1
        if board[x][y] < 0:
            board[x][y] = 0


N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

turn = 0; flag = False
while True:
    ices = []
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visit[i][j]:
                ices.append(bfs(i, j))

    if len(ices) >= 2: # 두 덩어리로 나뉘면 종료
        flag = True
        break

    if not ices: #분리되지 않고 모두 다 녹으면 종료
        break

    #얼음 녹이기
    ice_remove(ices[0])

    turn += 1


if flag:
    print(turn)
else:
    print(0)