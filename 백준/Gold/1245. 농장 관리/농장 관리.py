import sys
input = sys.stdin.readline

dx = (0, 0, -1, 1, -1, -1, 1, 1)
dy = (-1, 1, 0, 0, -1, 1, -1, 1)

def dfs(x, y):
    global flag
    visit[x][y] = True

    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] > board[x][y]: flag = False
            if not visit[nx][ny] and board[nx][ny] == board[x][y]: dfs(nx, ny)
    
N, M = map(int, input().strip().split())
board = []
for n in range(N): board.append(list(map(int, input().strip().split())))

visit = [[False] * M for n in range(N)]
ans = 0
for n in range(N):
    for m in range(M):
        if not visit[n][m] and board[n][m] > 0:
            flag = True
            dfs(n, m)
            if flag: ans += 1
print(ans)