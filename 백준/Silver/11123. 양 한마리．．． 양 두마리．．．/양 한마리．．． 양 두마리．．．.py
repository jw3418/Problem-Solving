import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(sx, sy):
    global board, visited, H, W

    queue = deque([]); queue.append((sx, sy))
    visited[sx][sy] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<H and 0<=ny<W:
                if not visited[nx][ny] and board[nx][ny] == '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))


T = int(input())
for t in range(T):
    H, W = map(int, input().split())
    board = []
    for h in range(H):
        row = list(input().strip())
        board.append(row)
    visited = [[False]*W for h in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and board[i][j] == '#':
                bfs(i, j)
                ans += 1
    print(ans)