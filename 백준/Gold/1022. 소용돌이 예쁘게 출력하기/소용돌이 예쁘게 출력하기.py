import sys
input = sys.stdin.readline

dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

r1, c1, r2, c2 = map(int, input().split())
board = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]

num = 1; cnt = 0
x, y = 0, 0
step = 1
direction = 0
while cnt < (r2-r1+1)*(c2-c1+1):
    for _ in range(2):
        for s in range(step):
            if r1<=x<=r2 and c1<=y<=c2: # 해당 경우에만 board에 기록
                board[x-r1][y-c1] = num
                cnt += 1
            num += 1
            x += dx[direction]; y += dy[direction]
        direction = (direction+1)%4
    step += 1

num = 0
for i in range(r2-r1+1): num = max(num, max(board[i]))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(board[i][j]).rjust(len(str(num))), end=" ")
    print()