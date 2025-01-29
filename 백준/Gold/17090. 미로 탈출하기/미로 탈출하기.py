import sys
sys.setrecursionlimit(600000)
input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M: return 1
    if visit[x][y] != -1: return visit[x][y]

    nx, ny = -1, -1
    if board[x][y] == 'U': nx, ny = x+dx[0], y+dy[0]
    elif board[x][y] == 'R': nx, ny = x+dx[1], y+dy[1]
    elif board[x][y] == 'D': nx, ny = x+dx[2], y+dy[2]
    elif board[x][y] == 'L': nx, ny = x+dx[3], y+dy[3]

    visit[x][y] = 0
    visit[x][y] = max(visit[x][y], dfs(nx, ny))
    return visit[x][y]


N, M = map(int, input().split())
board = [list(input().strip()) for n in range(N)]
visit = [[-1]*M for n in range(N)] #-1:방문안함, 0:방문함(탈출불가), 1:탈출가능
cnt = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == -1:
            if dfs(i, j) == 1:
                cnt += 1
        elif visit[i][j] == 1:
            cnt += 1
print(cnt)