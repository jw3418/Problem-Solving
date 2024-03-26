import sys
input = sys.stdin.readline

N = int(input())
board = [input().split() for n in range(N)]

dx = (0, 1); dy = (1, 0)

def dfs(x, y, tmp, prev):
    global max_, min_
    if (x, y) == (N-1, N-1): 
        max_ = max(max_, tmp)
        min_ = min(min_, tmp)
        return
    
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if 48 <= ord(board[nx][ny]) and ord(board[nx][ny]) <= 57:
                nex_tmp = 0
                if prev == '+': nex_tmp = tmp+int(board[nx][ny])
                elif prev == '-': nex_tmp = tmp-int(board[nx][ny])
                elif prev == '*': nex_tmp = tmp*int(board[nx][ny])
                dfs(nx, ny, nex_tmp, 0)
            else:
                dfs(nx, ny, tmp, board[nx][ny])

max_ = -int(10e9); min_ = int(10e9)
dfs(0, 0, int(board[0][0]), 0)
print(max_, min_)