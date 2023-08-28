import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(x, y):
    global max_docs_cnt, keys

    queue = deque([]); queue.append((x, y))
    visit = [[False] * W for h in range(H)]; visit[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if not visit[nx][ny]:
                    if board[nx][ny] == '.': #빈 공간
                        visit[nx][ny] = True
                        queue.append((nx, ny))

                    elif 97 <= ord(board[nx][ny]) <= 122: #열쇠 -> queue 초기화, visit 리스트 초기화
                        keys.add(board[nx][ny])
                        board[nx][ny] = '.'
                        queue = deque([])
                        visit = [[False] * W for h in range(H)]; visit[nx][ny] = True
                        queue.append((nx, ny))

                    elif 65 <= ord(board[nx][ny]) <= 90: #문
                        if chr(ord(board[nx][ny]) + 32) in keys:
                            visit[nx][ny] = True
                            board[nx][ny] = '.'
                            queue.append((nx, ny))

                    elif board[nx][ny] == '$': #문서
                        max_docs_cnt += 1
                        visit[nx][ny] = True
                        board[nx][ny] = '.'
                        queue.append((nx, ny))


T = int(sys.stdin.readline()[:-1])
for t in range(T):
    H, W = map(int, sys.stdin.readline()[:-1].split())

    board = deque([])
    for h in range(H):
        board.append(deque(list(sys.stdin.readline()[:-1])))
    
    keys = set(list(sys.stdin.readline()[:-1]))

    for i in range(H):
        board[i].appendleft('.'); board[i].append('.')
    board.appendleft(deque(['.' for w in range(W+2)])); board.append(deque(['.' for w in range(W+2)]))

    H += 2; W += 2
    max_docs_cnt = 0
    bfs(0, 0)
    
    print(max_docs_cnt)