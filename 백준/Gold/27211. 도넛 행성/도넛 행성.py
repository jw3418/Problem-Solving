import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(x, y):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            nx = (nx+N)%N; ny = (ny+M)%M
            if board[nx][ny] == 0 and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny))

N, M = map(int, input().split())
board = [list(map(int, input().strip().split())) for n in range(N)]
visit = [[False]*M for n in range(N)]

answer = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == 0 and not visit[n][m]:
            bfs(n, m)
            answer += 1
print(answer)