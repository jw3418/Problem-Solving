import sys
from collections import deque

N, M = map(int, sys.stdin.readline()[:-1].split())
board = [list(map(int, list(sys.stdin.readline()[:-1]))) for n in range(N)]

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def grouping(x, y, number):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True; board[x][y] = number

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and board[nx][ny] == 0:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    board[nx][ny] = number; cnt += 1
    return cnt

def get_sum(x, y):
    sum_ = 1; visit = set()
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] > 0 and board[nx][ny] not in visit:  
                sum_ += group_info[board[nx][ny]]
                visit.add(board[nx][ny])
    answer[x][y] = sum_ % 10

for i in range(N):
    for j in range(M):
        if board[i][j] == 1: board[i][j] = -1

group_info = dict(); visit = [[False]*M for n in range(N)]; number = 1
for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] == 0:
            group_info[number] = grouping(i, j, number)
            number += 1

answer = [[0]*M for n in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            get_sum(i, j)

for n in range(N):
    print("".join(map(str, answer[n])))