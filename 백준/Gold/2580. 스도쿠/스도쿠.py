import sys

def checkRow(i, x):
    for y in range(9):
        if board[x][y] == i:
            return False
    return True

def checkCol(i, y):
    for x in range(9):
        if board[x][y] == i:
            return False
    return True

def checkSquare(i, x, y): #0,1,2
    x = (x // 3) * 3; y = (y // 3) * 3
    for a in range(x, x+3):
        for b in range(y, y+3):
            if board[a][b] == i:
                return False
    return True

def dfs(idx):
    if idx == len(zero):
        for a in range(9):
            for b in range(9):
                print(board[a][b], end=" ")
            print()
        exit()
    
    x = zero[idx][0]; y = zero[idx][1]
    for i in range(1, 10): #zero의 위치에 1~9까지 넣기
        if checkRow(i, x) and checkCol(i, y) and checkSquare(i, x, y): #해당 조건이 충족되는 경우 dfs
            board[x][y] = i
            dfs(idx + 1)
            board[x][y] = 0 #for backtracking

board = []; zero = []
for i in range(9):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    board.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            zero.append([i, j])

dfs(0) #zero의 처음부터 시작