import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(x, y):
    queue = deque([]); queue.append((x, y))
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True
    C_coor = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                if board[nx][ny] != 0:
                    board[nx][ny] += 1

    for i in range(N):
        for j in range(M):
            if board[i][j] >= 3:
                C_coor.append((i, j))
            elif board[i][j] == 2:
                board[i][j] = 1
    return C_coor

def remove(C):
    for x, y in C:
        board[x][y] = 0
    


N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

turn = 0
while True:
    ##### 'C' 구하기
    C = bfs(0, 0)
    # print(C)
    # print()
    # for i in range(N):
    #     for j in range(M):
    #         print(board[i][j], end=" ")
    #     print()
    # break
    ##### 반환받은 'C'의 좌표가 없다면 종료
    if not C:
        break

    ##### 'C' 제거
    remove(C)

    turn += 1
print(turn)