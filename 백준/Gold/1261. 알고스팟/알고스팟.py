import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([]); queue.append((0, 0))
    visit[0][0] = 0

    while queue:
        curr = queue.popleft()

        if curr[0] == N-1 and curr[1] == M-1:
            print(visit[N-1][M-1])
            return
        
        for i in range(4):
            nx = curr[0] + dx[i]; ny = curr[1] + dy[i]

            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and visit[nx][ny] == -1:
                if Map[nx][ny] == 1:
                    visit[nx][ny] = visit[curr[0]][curr[1]] + 1
                    queue.append((nx, ny))
                else:
                    visit[nx][ny] = visit[curr[0]][curr[1]]
                    queue.appendleft((nx, ny))


M, N = map(int, input().split(' '))

Map = []
for n in range(N):
    Map.append(list(map(int, list(sys.stdin.readline()[:-1]))))

visit = [[-1] * M for _ in range(N)]
bfs()