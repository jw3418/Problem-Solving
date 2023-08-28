from collections import deque

N = int(input()); board = [[0] * N for _ in range(N)] # 기본값:0, 뱀의위치:1, 사과위치:2
K = int(input())
for i in range(K):
    tmp = list(map(int, input().split(' ')))
    board[tmp[0]-1][tmp[1]-1] = 2

L = int(input()); turn = {} # 방향 전환 시점
for i in range(L):
    tmp = input().split(' ')
    turn[int(tmp[0])] = tmp[1]

x, y = 0, 0
snake = deque(()); snake.append((x, y)) # 뱀의 위치 (snake[-1]이 머리, snake[0]이 꼬리)
board[x][y] = 1
dx = [0, 1, 0, -1] # 위아래로 한쌍
dy = [1, 0, -1, 0] # 위아래로 한쌍
direction = 0

def rotate(value):
    global direction
    if value == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

cnt = 0 # 시간 초
while True: #1)벽이나 자기 몸에 닿는지 확인 2)이동 + 사과인지 확인 + 이동 후 방향 전환 해야하는지 확인
    cnt += 1
    x += dx[direction]; y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N:
        break

    if board[x][y] == 2:
        board[x][y] = 1
        snake.append((x, y))
        if cnt in turn:
            rotate(turn[cnt])
    elif board[x][y] == 0:
        board[x][y] = 1
        snake.append((x, y))
        tmp_x, tmp_y = snake.popleft()
        board[tmp_x][tmp_y] = 0
        if cnt in turn:
            rotate(turn[cnt])
    else:
        break

print(cnt)