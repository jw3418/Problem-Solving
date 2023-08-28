import sys
from collections import deque

#좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

percent0 = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 'a', 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
percent1 = list(reversed(list(map(list, zip(*percent0)))))
percent2 = list(reversed(list(map(list, zip(*percent1)))))
percent3 = list(reversed(list(map(list, zip(*percent2)))))
percent = [percent0, percent1, percent2, percent3]

def move(x, y, p_idx):
    origin = float(board[x][y])
    local_out_sand = 0; alpha = []; total_sand = 0
    for i in range(5):
        for j in range(5):
            if 0 <= x-2+i < N and 0 <= y-2+j < N:
                if percent[p_idx][i][j] != 'a' and percent[p_idx][i][j] != 0:
                    board[x-2+i][y-2+j] += int(percent[p_idx][i][j] * origin)
                    total_sand += int(percent[p_idx][i][j] * origin)
                elif percent[p_idx][i][j] == 'a':
                    alpha = [x-2+i, y-2+j, True]
            else:
                if percent[p_idx][i][j] != 'a' and percent[p_idx][i][j] != 0:
                    local_out_sand += int(percent[p_idx][i][j] * origin)
                    total_sand += int(percent[p_idx][i][j] * origin)
                elif percent[p_idx][i][j] == 'a':
                    alpha = [x-2+i, y-2+j, False]
    if alpha[2]:
        board[alpha[0]][alpha[1]] += int(origin) - total_sand
    else:
        local_out_sand += int(origin) - total_sand
  
    return local_out_sand


N = int(sys.stdin.readline()[:-1])
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

direction = []; mul = 1
for n in range(N*2 - 1):
    for i in range(mul):
        direction.append(n%4)
    if (n+1) % 2 == 0:
        mul += 1

queue = deque([[N//2, N//2]])
out_sand = 0
for idx in range(len(direction) - 1): #한 칸씩 이동
    x, y = queue.popleft()
    d_idx = direction[idx]

    nx = x + dx[d_idx]; ny = y + dy[d_idx]

    out_sand += move(nx, ny, d_idx)

    queue.append([nx, ny])

print(out_sand)