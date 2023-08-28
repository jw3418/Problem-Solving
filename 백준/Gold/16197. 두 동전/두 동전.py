import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(coins):
    queue = deque([])
    queue.append(coins)

    while queue:
        coin1, coin2, cnt = queue.popleft()
        x1, y1 = coin1; x2, y2 = coin2

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]; ny1 = y1 + dy[i]; nx2 = x2 + dx[i]; ny2 = y2 + dy[i]
            if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1 #그대로 있어야함
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2 #그대로 있어야함
                queue.append([(nx1, ny1), (nx2, ny2), cnt + 1]) #떨어지지 않은 경우 queue에 append
            elif (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M) and (0 <= nx2 < N and 0 <= ny2 < M): #coin1이 떨어지는 경우
                return cnt + 1
            elif (nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M) and (0 <= nx1 < N and 0 <= ny1 < M): #coin2가 떨어지는 경우
                return cnt + 1
            

N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline()[:-1]))

coins = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))

coins.append(0) #[(x1, y1), (x2, y2), cnt]
result = bfs(coins)
print(result)