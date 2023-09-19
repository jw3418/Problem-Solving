import sys
import copy
from collections import deque

dx = (0, 0, 0, -1, 1)
dy = (0, 1, -1, 0, 0)

R, C, K = map(int, sys.stdin.readline()[:-1].split())
K_check = set(); heaters = []
for r in range(R):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    for c in range(C): #1:오른쪽, 2:왼쪽, 3:위, 4:아래
        if 1 <= tmp[c] <= 4: heaters.append((tmp[c], r, c))
        elif tmp[c] == 5: K_check.add((r, c))

W = int(sys.stdin.readline()[:-1]); wall = [[set() for _ in range(C)] for _ in range(R)]
for w in range(W): x, y, t = map(int, sys.stdin.readline()[:-1].split()); wall[x-1][y-1].add(t)

board = [[0]*C for _ in range(R)]

def heaterOn(direction, x, y):
    queue = deque([]); visit = [[False]*C for _ in range(R)]

    if direction == 1: #오른쪽
        queue.append([x, y+1, 5])
        while queue:
            x, y, t = queue.popleft()
            if visit[x][y]: continue
            visit[x][y] = True
            board[x][y] += t

            if t > 1:
                if 0 <= x < R and 0 <= y+1 < C:
                    if 1 not in wall[x][y]:
                        queue.append([x, y+1, t-1])
                if 0 <= x-1 < R and 0 <= y+1 < C:
                    if 0 not in wall[x][y] and 1 not in wall[x-1][y]:
                        queue.append([x-1, y+1, t-1])
                if 0 <= x+1 < R and 0 <= y+1 < C:
                    if 0 not in wall[x+1][y] and 1 not in wall[x+1][y]:
                        queue.append([x+1, y+1, t-1])

    elif direction == 2: #왼쪽 
        queue.append([x, y-1, 5])
        while queue:
            x, y, t = queue.popleft()
            if visit[x][y]: continue
            visit[x][y] = True
            board[x][y] += t

            if t > 1:
                if 0 <= x < R and 0 <= y-1 < C:
                    if 1 not in wall[x][y-1]:
                        queue.append([x, y-1, t-1])
                if 0 <= x-1 < R and 0 <= y-1 < C:
                    if 0 not in wall[x][y] and 1 not in wall[x-1][y-1]:
                        queue.append([x-1, y-1, t-1])
                if 0 <= x+1 < R and 0 <= y-1 < C:
                    if 0 not in wall[x+1][y] and 1 not in wall[x+1][y-1]:
                        queue.append([x+1, y-1, t-1])

    elif direction == 3: #위쪽
        queue.append([x-1, y, 5])
        while queue:
            x, y, t = queue.popleft()
            if visit[x][y]: continue
            visit[x][y] = True
            board[x][y] += t

            if t > 1:
                if 0 <= x-1 < R and 0 <= y < C:
                    if 0 not in wall[x][y]:
                        queue.append([x-1, y, t-1])
                if 0 <= x-1 < R and 0 <= y-1 < C:
                    if 0 not in wall[x][y-1] and 1 not in wall[x][y-1]:
                        queue.append([x-1, y-1, t-1])
                if 0 <= x-1 < R and 0 <= y+1 < C:
                    if 0 not in wall[x][y+1] and 1 not in wall[x][y]:
                        queue.append([x-1, y+1, t-1])

    elif direction == 4: #아래쪽
        queue.append([x+1, y, 5])
        while queue:
            x, y, t = queue.popleft()
            if visit[x][y]: continue
            visit[x][y] = True
            board[x][y] += t

            if t > 1:
                if 0 <= x+1 < R and 0 <= y < C:
                    if 0 not in wall[x+1][y]:
                        queue.append([x+1,y,t-1])
                if 0 <= x+1 < R and 0 <= y-1 < C:
                    if 1 not in wall[x][y-1] and 0 not in wall[x+1][y-1]:
                        queue.append([x+1,y-1,t-1])
                if 0 <= x+1 < R and 0 <= y+1 < C:
                    if 1 not in wall[x][y] and 0 not in wall[x+1][y+1]:
                        queue.append([x+1,y+1,t-1])

chocolate = 0
while True:
    if chocolate > 100: print(101); exit()

    # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    for heater in heaters:
        heaterOn(heater[0], heater[1], heater[2])

    # 2. 온도가 조절됨
    diffs = []
    for x in range(R):
        for y in range(C):
            for i in range(1, 5):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    diff = (board[x][y] - board[nx][ny]) // 4
                    if diff > 0:
                        if i == 1 and 1 in wall[x][y]: continue #오른쪽
                        if i == 2 and 1 in wall[nx][ny]: continue #왼쪽
                        if i == 3 and 0 in wall[x][y]: continue #위쪽
                        if i == 4 and 0 in wall[nx][ny]: continue #아래쪽
                        diffs.append([x, y, -diff]); diffs.append([nx, ny, diff])

    for _ in range(len(diffs)):
        x, y, diff = diffs[_]; board[x][y] += diff

    # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    for r in range(R):
        for c in range(C):
            if r == 0 or r == R-1 or c == 0 or c == C-1:
                if board[r][c] > 0: board[r][c] -= 1

    # 4. 초콜릿을 하나 먹는다
    chocolate += 1

    # 5. 조사하는 모든 칸의 온도가 K이상이 되었는 지 검사
    count = 0
    for check in K_check:
        if board[check[0]][check[1]] >= K: count += 1
    if count == len(K_check): break

print(chocolate)