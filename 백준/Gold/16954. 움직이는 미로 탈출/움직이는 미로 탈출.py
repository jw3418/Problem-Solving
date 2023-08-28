import sys
from collections import deque

dx = [0, 0, -1, 1, 1, 1, -1, -1, 0]
dy = [-1, 1, 0, 0, 1, -1, 1, -1, 0]

def bfs():
    queue = deque()
    queue.append([7, 0])

    turn = 0
    while queue:
        visit = [[False] * 8 for _ in range(8)] #중복 제거 및 시간 단축을 위함
        for _ in range(len(queue)): #한번의 turn
            x, y = queue.popleft()
            if x == 0 and y == 7:
                return True
            if board[x][y] == '.':
                for i in range(9):
                    nx = x + dx[i]; ny = y + dy[i]
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny] == '.' and not visit[nx][ny]:
                            queue.append([nx, ny])
                            visit[nx][ny] = True

        board.pop()
        board.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])
        turn += 1
        if turn == 9:
            return True

    return False

board = deque([])
for _ in range(8):
    board.append(list(sys.stdin.readline()[:-1]))

if bfs():
    print(1)
else:
    print(0)