import sys
from collections import deque
input = sys.stdin.readline

dx = (0, -1, 0, 1)
dy = (-1, 0, 1, 0)

N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for m in range(M)]
visit = [[False]*N for m in range(M)]

def bfs(x, y):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True

    roomSize = 1
    while queue:
        x, y = queue.popleft()
        wall = 1
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if (board[x][y]&wall) != wall: #뚫려있는 경우
                if 0<=nx<M and 0<=ny<N and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    roomSize+=1
            wall*=2
    return roomSize

one, two, three = 0, 0, 0
for i in range(M):
    for j in range(N):
        if not visit[i][j]:
            one += 1
            two = max(two, bfs(i, j))

for i in range(M):
    for j in range(N):
        wall = 1
        while wall<=8:
            if board[i][j]&wall: #벽이 있는 경우
                    visit = [[False]*N for m in range(M)]
                    board[i][j] -= wall
                    three = max(three, bfs(i, j))
                    board[i][j] += wall
            wall*=2
print(one); print(two); print(three)