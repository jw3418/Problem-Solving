import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def backtracking(o_cnt):
    global answer

    if o_cnt == 3:
        if check():
            answer = True; return
    else:
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'X':
                    board[i][j] = 'O'
                    backtracking(o_cnt+1)
                    board[i][j] = 'X'

def check():
    q = deque(teachers)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            while 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 'S': return False
                elif board[nx][ny] == 'T' or board[nx][ny] == 'O': break
                nx += dx[i]; ny += dy[i]
    return True

N = int(sys.stdin.readline()[:-1])
board = [list(sys.stdin.readline()[:-1].split()) for n in range(N)]

teachers = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i, j))

answer = False
backtracking(0)
if answer: print("YES")
else: print("NO")