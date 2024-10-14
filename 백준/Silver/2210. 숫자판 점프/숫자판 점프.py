import sys
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def dfs(x, y, num):
    global result
    if len(num) == 6:
        result.append(num)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, num+str(board[nx][ny]))

board = [list(map(int, input().split())) for _ in range(5)]
result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, "")
result = set(result)
print(len(result))