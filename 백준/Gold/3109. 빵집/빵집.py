import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for r in range(R): board.append(list(input().strip()))

dr = (-1, 0, 1)
dc = (1, 1, 1)

def dfs(r, c):
    if c == C-1: return True
    for i in range(3):
        nr = r+dr[i]; nc = c+dc[i]
        if 0<=nr<R and 0<=nc<C:
            if board[nr][nc] == '.' and not visit[nr][nc]:
                visit[nr][nc] = True
                if dfs(nr, nc): return True
    return False

cnt = 0
visit = [[False]*C for r in range(R)]
for r in range(R):
    if dfs(r, 0): cnt += 1
print(cnt)