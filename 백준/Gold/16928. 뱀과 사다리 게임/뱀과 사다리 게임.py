import sys
from collections import deque

def bfs():
    global min_cnt
    queue = deque(); queue.append(1)

    while queue:
        pos = queue.popleft()
        if pos == 100:
            min_cnt = board[pos]
            break
        for i in range(1, 7): # 주사위 굴리기
            npos = pos + i
            if npos <= 100 and board[npos] == 0:
                if npos in ladder:
                    npos = ladder[npos]
                if npos in snake:
                    npos = snake[npos]
                if board[npos] == 0:
                    board[npos] = board[pos] + 1
                    queue.append(npos)


N, M = map(int, sys.stdin.readline()[:-1].split())
ladder = dict()
for n in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    ladder[tmp[0]] = tmp[1]
snake = dict()
for m in range(M):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    snake[tmp[0]] = tmp[1]

min_cnt = 10e9
board = [0 for _ in range(101)]
visit = [False for _ in range(101)]
bfs()
print(min_cnt)