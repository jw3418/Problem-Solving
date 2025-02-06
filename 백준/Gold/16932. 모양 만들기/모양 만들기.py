import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for n in range(N)]

def dfs(x, y):
    global num, cnt
    
    cnt += 1
    color[x][y] = num
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0<=nx<N and 0<=ny<M:
            if color[nx][ny] == 0 and board[nx][ny] == 1:
                dfs(nx, ny)



color = [[0]*M for n in range(N)]; dict_ = dict()
num = 1
for i in range(N):
    for j in range(M):
        if color[i][j] == 0 and board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            dict_[num] = cnt
            num += 1

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            tmp = 1; set_ = set()
            for d in range(4):
                ni, nj = i+dx[d], j+dy[d]
                if 0<=ni<N and 0<=nj<M:
                    if color[ni][nj] != 0:
                        if color[ni][nj] not in set_:
                            tmp += dict_[color[ni][nj]]
                        set_.add(color[ni][nj])
            ans = max(ans, tmp)
print(ans)