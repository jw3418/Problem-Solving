import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([])
    queue.append([x, y, -1])
    visit[x][y] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == dest[0] and y == dest[1]:
            return cnt
        
        for i in range(4):
            nx = x; ny = y
            while True: #해당 방향으로 최대한 감
                nx += dx[i]; ny += dy[i]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    break
                if board[nx][ny] == '*':
                    break
                if not visit[nx][ny]: #해당 방향으로 더 갈 수 있는 경우
                    queue.append([nx, ny, cnt+1])
                    visit[nx][ny] = True
            


W, H = map(int, sys.stdin.readline()[:-1].split())
board = []; src_dest = []
for h in range(H):
    tmp = list(sys.stdin.readline()[:-1])
    for w in range(W):
        if tmp[w] == 'C':
            src_dest.append([h, w])
    board.append(tmp)
src, dest = src_dest

visit = [[False] * W for _ in range(H)]
print(bfs(src[0], src[1]))