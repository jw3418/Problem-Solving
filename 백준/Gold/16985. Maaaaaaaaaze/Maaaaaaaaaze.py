import sys
from collections import deque
from itertools import permutations

dx = (1, -1, 0, 0, 0, 0)
dy = (0, 0, 1, -1, 0, 0)
dz = (0, 0, 0, 0, 1, -1)

def bfs():
    global answer

    queue = deque([]); queue.append((0, 0, 0, 0))
    visit = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]; visit[0][0][0] = True

    while queue:
        x, y, z, cnt = queue.popleft()
        if (x, y, z) == (4, 4, 4):
            answer = min(answer, cnt)

        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                if not visit[nz][nx][ny] and miros[nz][nx][ny] == 1:
                    visit[nz][nx][ny] = True
                    queue.append((nx, ny, nz, cnt+1))

def dfs(depth): #미로 한판 돌리기
    if depth == 5:
        if miros[0][0][0] == 1 and miros[4][4][4] == 1:
            bfs()
        return
    for i in range(4): #미로 한판 돌리기 (0도, 90도, 180도 270도)
        dfs(depth+1)
        miros[depth] = list(reversed(list(map(list, zip(*miros[depth])))))


boards = []; miros = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
for n in range(5):
    board = []
    for i in range(5):
        board.append(list(map(int, sys.stdin.readline()[:-1].split())))
    boards.append(board)

board_idx = [0, 1, 2, 3, 4]; answer = int(10e9)
for candi_idx in permutations(board_idx, 5): #층 순서 정하기
    for i in range(5):
        miros[candi_idx[i]] = boards[i]
    dfs(0)
if answer == int(10e9): print(-1)
else: print(answer)