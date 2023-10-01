import sys

#NWES
dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)
direction = {'N':0, 'W':1, 'E':2, 'S':3}

A, B = map(int, sys.stdin.readline()[:-1].split()); N, M = map(int, sys.stdin.readline()[:-1].split())

board = [[0]*A for _ in range(B)]; robot = dict()
for n in range(1, N+1):
    y, x, d = sys.stdin.readline()[:-1].split(); x = int(x); y = int(y); x = B-x; y -= 1
    board[x][y] = n; robot[n] = [x, y, d]

for m in range(M):
    num, cmd, iteration = sys.stdin.readline()[:-1].split(); num = int(num); iteration = int(iteration)
    if cmd == 'L':
        iteration %= 4
        for _ in range(iteration):
            d = robot[num][2]
            if d == 'N': robot[num][2] = 'W'
            elif d == 'W': robot[num][2] = 'S'
            elif d == 'E': robot[num][2] = 'N'
            elif d == 'S': robot[num][2] = 'E'
    elif cmd == 'R':
        iteration %= 4
        for _ in range(iteration):
            d = robot[num][2]
            if d == 'N': robot[num][2] = 'E'
            elif d == 'W': robot[num][2] = 'N'
            elif d == 'E': robot[num][2] = 'S'
            elif d == 'S': robot[num][2] = 'W'
    elif cmd == 'F':
        for _ in range(iteration):
            x = robot[num][0]; y = robot[num][1]; d = robot[num][2]
            nx = x + dx[direction[d]]; ny = y + dy[direction[d]]
            if 0 <= nx < B and 0 <= ny < A:
                if board[nx][ny] != 0:
                    print("Robot "+str(num)+" crashes into robot "+str(board[nx][ny])); exit()
                else:
                    board[x][y] = 0; board[nx][ny] = num
                    robot[num] = [nx, ny, d]
            else:
                print("Robot "+str(num)+" crashes into the wall"); exit()
print("OK")