import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, input().split())
board = []
for n in range(N): board.append(list(input().strip()))

def dfs(x, y):
    global ans
    visit[x][y] = True
    if board[x][y] == 'P':
        ans += 1
    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if not visit[nx][ny] and board[nx][ny] != 'X':
                dfs(nx, ny)
        
ans = 0
visit = [[False]*M for n in range(N)]
for x in range(N):
    for y in range(M):
        if board[x][y] == 'I':
            dfs(x, y)
if ans == 0: print('TT')
else: print(ans)