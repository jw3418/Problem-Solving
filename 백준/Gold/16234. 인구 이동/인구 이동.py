import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
    global count, total
    queue = deque([])
    queue.append([a, b])
    visit[a][b] = True
    coor.add((a, b))

    result = []
    while queue:
        x, y = queue.popleft()
        count += 1; total += world[x][y]
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(world[x][y] - world[nx][ny]) <= R and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append([nx, ny])
                    coor.add((nx, ny))


N, L, R = map(int, sys.stdin.readline()[:-1].split())
world = []
for n in range(N):
    world.append(list(map(int, sys.stdin.readline()[:-1].split())))

result = 0
while True:
    visit = [[False for _ in range(N)] for _ in range(N)]
    state = []
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                count = 0; total = 0; coor = set()
                bfs(i, j)
                if count > 1:
                    state.append([count, total, coor])

    if len(state) == 0:
        break
    else:
        for _ in range(len(state)):
            tmp = state[_][1] // state[_][0]
            for i in range(N):
                for j in range(N):
                    if (i, j) in state[_][2]:
                        world[i][j] = tmp

    result += 1
print(result)