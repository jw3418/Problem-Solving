import sys

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

R, C, K = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for r in range(R)]
visit = [[False for c in range(C)] for r in range(R)]

def dfs(depth, x, y):
    global answer

    if depth >= K:
        if depth == K and (x, y) == (0, C-1): answer += 1
        return
    else:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] != 'T' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    dfs(depth+1, nx, ny)
                    visit[nx][ny] = False

visit[R-1][0] = True
answer = 0
dfs(1, R-1, 0)
print(answer)