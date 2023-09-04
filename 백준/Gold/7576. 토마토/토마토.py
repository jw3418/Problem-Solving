import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque([])
    for _ in range(len(first_one)):
        queue.append(first_one[_])

    while queue:
        x, y = map(int, queue.popleft())

        for i in range(4): #상하좌우 탐색
            nx = x + dx[i]; ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if Map[nx][ny] == 0:
                Map[nx][ny] = Map[x][y] + 1
                queue.append([nx, ny])

M, N = map(int, sys.stdin.readline()[:-1].split(' '))
Map = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split(' ')))
    Map.append(tmp)

first_one = []
for x in range(N):
    for y in range(M): #1에서부터 동시에 bfs를 시작해야함
        if Map[x][y] == 1:
            first_one.append([x, y])

bfs(); date = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            print(-1); exit()
    date = max(max(Map[i]), date)
print(date-1)