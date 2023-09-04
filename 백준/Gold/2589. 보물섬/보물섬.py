import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global local_result
    queue = deque([])
    queue.append((x, y, 0))
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True

    while queue:
        x, y, cnt = queue.popleft()
        local_result = max(result, cnt)
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 'L' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny, cnt+1))
    return


N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(sys.stdin.readline()[:-1]))

result = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == 'L':
            local_result = 0
            bfs(n, m)
            result = max(result, local_result)
print(result)