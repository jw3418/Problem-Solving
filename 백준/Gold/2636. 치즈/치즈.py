import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(x, y):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True

    c_board = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                elif board[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    board[nx][ny] = 'c'
                    c_board.append((nx, ny))
    
    return c_board

def c_remove(c_board):
    for x, y in c_board:
        board[x][y] = 0



R, C = map(int, sys.stdin.readline()[:-1].split())
board = []
for r in range(R):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

turn = 0; c_cnt = 0
while True:
    #가장 왼쪽위는 무조건 빈 공간임 여기서에 bfs를 시작하여 녹는 부분을 c로 바꿔줌
    visit = [[False] * C for _ in range(R)]
    c_board = bfs(0, 0)

    if not c_board:
        break

    c_cnt = len(c_board)

    #치즈조각 녹이기
    c_remove(c_board)

    turn += 1



print(turn)
print(c_cnt)