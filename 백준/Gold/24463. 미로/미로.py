import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def dfs(x, y):
    if (x, y) == hole[1]: return True
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and board[nx][ny] == '@':
            board[nx][ny] = '.'
            if dfs(nx, ny): return True
            board[nx][ny] = '@'
    return False

N, M = map(int, input().strip().split())
board = []; hole = []
for n in range(N):
    tmp = list(input().strip())
    for m in range(M):
        if tmp[m] == '.':
            if n==0 or n==N-1 or m==0 or m==M-1: hole.append((n, m))
            tmp[m] = '@'
    board.append(tmp)

dfs(hole[0][0], hole[0][1])
board[hole[0][0]][hole[0][1]] = '.'
for n in range(N): print(''.join(map(str, board[n])))