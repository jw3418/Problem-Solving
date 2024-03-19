import sys
from collections import deque
input = sys.stdin.readline

def indexing():
    x, y = N//2, N//2
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    step = 0

    while True:
        for i in range(4):
            if i%2==0: step += 1
            for j in range(step):
                x+=dx[i]; y+=dy[i]
                coor.append((x, y))
                if x==0 and y==0: return

def blizzard(d, s):
    x, y = N//2, N//2
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for _ in range(s):
        x+=dx[d]; y+=dy[d]
        if 0<=x<N and 0<=y<N:
            board[x][y] = 0

    empty()
    while bomb(): empty()
    group()

def empty():
    bcoor = deque()
    for x, y in coor:
        if board[x][y] == 0: bcoor.append((x, y))
        elif bcoor:
            bx, by = bcoor.popleft()
            board[bx][by] = board[x][y]
            board[x][y] = 0
            bcoor.append((x, y))

def bomb():
    cnt = 0
    will_bombed = deque()
    num = -1
    flag = False
    for x, y in coor:
        if board[x][y] == num:
            cnt += 1
            will_bombed.append((x, y))
        else:
            if cnt >= 4:
                flag = True
                score[num-1] += cnt
                while will_bombed:
                    bx, by = will_bombed.popleft()
                    board[bx][by] = 0
            cnt = 1
            num = board[x][y]
            will_bombed = deque(); will_bombed.append((x, y))
    return flag

def group():
    global board
    cnt = 0; num = -1
    result = []
    for x, y in coor:
        if board[x][y] == num:
            cnt += 1
        else:
            if num != -1: result.append(cnt); result.append(num)
            cnt = 1
            num = board[x][y]

    board = [[0]*N for n in range(N)]
    i = 0
    for x, y in coor:
        if i < len(result):
            board[x][y] = result[i]
            i+=1


N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for n in range(N)]
score = [0]*3

coor = deque()
indexing()

for m in range(M):
    d, s = map(int, input().strip().split())
    d -= 1
    blizzard(d, s)

ans = 0
for i in range(1, 4): ans += i*score[i-1]
print(ans)