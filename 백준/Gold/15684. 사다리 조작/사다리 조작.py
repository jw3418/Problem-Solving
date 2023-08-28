import sys
from collections import deque

def is_complete():
    for j in range(N): #모든 세로선을 순회
        check = j
        for i in range(H):
            if board[i][check]:
                check += 1
            elif check > 0 and board[i][check-1]:
                check -= 1
        if check != j: #같은 세로선 위치로 도착하지 않은 경우 False 반환
            return False
    return True

def backtracking(depth, x, y): #depth는 추가한 사다리의 개수
    global result

    if depth > 3:
        return
    elif is_complete():
        result = min(result, depth)
        return

    for i in range(x, H):
        if i == x: startY = y
        else: startY = 0
        for j in range(startY, N - 1):
            if not board[i][j] and not board[i][j+1]:
                if j > 0 and board[i][j-1]:
                    continue
                board[i][j] = True
                backtracking(depth + 1, i, j+2)
                board[i][j] = False


N, M, H = list(map(int, sys.stdin.readline()[:-1].split())) #N: 세로선 개수, M: 가로선 개수, H: 가로선을 놓을 수 있는 위치 개수

board = [[False] * N for _ in range(H)]
if M == 0:
    print(0); exit()

for m in range(M):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    tmp[0] -= 1; tmp[1] -= 1
    board[tmp[0]][tmp[1]] = True #tmp[0]:가로선의 행번호, tmp[1]:시작점의 열번호

result = 4
backtracking(0, 0, 0)
if result < 4:
    print(result)
else:
    print(-1)