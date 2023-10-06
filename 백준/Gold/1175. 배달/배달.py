import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

board = [list(input()[:-1]) for n in range(N)]

start = tuple(); flag = False
for i in range(N):
    for j in range(M):
        if board[i][j] == 'S': start = (i, j)
        elif board[i][j] == 'C':
            if not flag: board[i][j] = 'C1'; flag = True
            else: board[i][j] = 'C2'

queue = deque([]); queue.append((start[0], start[1], 4, 0, 0))
visit = [[[[[False for j in range(2)] for i in range(2)] for m in range(M)] for n in range(N)] for d in range(5)] # [direction][x][y][C1][C2]
visit[4][start[0]][start[1]][0][0] = True

answer = 0
while queue:
    size = len(queue)
    for s in range(size):
        x, y, pre_dir, flag1, flag2 = queue.popleft()

        if flag1 == 1 and flag2 == 1:
            print(answer); exit()

        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]; nflag1 = flag1; nflag2 = flag2 #nflag1, nflag2로 따로 할당해줘야함! node 별로 독립적인거니까..
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#' and i != pre_dir:
                if not visit[i][nx][ny][flag1][flag2]:
                    if board[nx][ny] == 'C1': nflag1 = 1
                    elif board[nx][ny] == 'C2': nflag2 = 1
                    visit[i][nx][ny][nflag1][nflag2] = True
                    queue.append((nx, ny, i, nflag1, nflag2))
    answer += 1
print(-1)