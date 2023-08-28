import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque([])
    queue.append([0, 0, 0])
    visit[0][0][0] = 1

    while queue:
        currX, currY, wall = queue.popleft()
        if currX == N-1 and currY == M-1:
            print(visit[currX][currY][wall])
            return
        for i in range(4):
            nextX = currX + dx[i]; nextY = currY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < M:
                if board[nextX][nextY] == 0 and visit[nextX][nextY][wall] == 0: #벽 부수지 않는 경우
                    visit[nextX][nextY][wall] = visit[currX][currY][wall] + 1
                    queue.append([nextX, nextY, wall])
                elif board[nextX][nextY] == 1 and visit[nextX][nextY][wall] == 0 and wall == 0: #벽 부수는 경우
                    visit[nextX][nextY][1] = visit[currX][currY][wall] + 1
                    queue.append([nextX, nextY, 1])
    print(-1)
        

N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, list(sys.stdin.readline()[:-1]))))

visit = [[[0, 0] for _ in range(M)] for _ in range(N)] # visit 리스트를 3차원으로 선언하여 벽을 부쉈는지, 부수지 않았는 지의 두 가지 경우를 check
bfs()