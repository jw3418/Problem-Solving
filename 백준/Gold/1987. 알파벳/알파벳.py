import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, trace):
    global maxLen
    maxLen = max(len(trace), maxLen)

    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in trace:
                trace.add(board[nx][ny])
                dfs(nx, ny, trace)
                trace.remove(board[nx][ny])

R, C = map(int, sys.stdin.readline()[:-1].split())
board = []
for r in range(R):
    board.append(list(sys.stdin.readline()[:-1]))

trace = set(board[0][0]); maxLen = 1
dfs(0, 0, trace)
print(maxLen)