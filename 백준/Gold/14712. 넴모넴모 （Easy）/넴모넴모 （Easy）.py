import sys
input = sys.stdin.readline

def dfs(x, y):
    global Cnt

    if (x, y) == (N+1, 1):
        Cnt += 1; return
    elif y == M: #오른쪽 이동 불가
        nx, ny = x+1, 1
    else:
        nx, ny = x, y+1

    dfs(nx, ny) #넴모 안놓는 경우
    if board[x-1][y-1] == 0 or board[x-1][y] == 0 or board[x][y-1] == 0:
        board[x][y] = 1
        dfs(nx, ny)
        board[x][y] = 0

N, M = map(int, input().split())
board = [[0]*(M+1) for n in range(N+1)]
Cnt = 0
dfs(1, 1)
print(Cnt)