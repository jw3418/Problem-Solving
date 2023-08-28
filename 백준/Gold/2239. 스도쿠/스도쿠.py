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

def checkSquare(i, x, y):
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
                print(board[a][b], end="")
            print()
        exit()

    x = zero[idx][0]; y = zero[idx][1]
    for i in range(1, 10):
        if checkRow(i, x) and checkCol(i, y) and checkSquare(i, x, y):
            board[x][y] = i
            dfs(idx + 1)
            board[x][y] = 0


board = []; zero = []
for _ in range(9):
    tmp = list(map(int, sys.stdin.readline()[:9]))
    for i in range(9):
        if tmp[i] == 0:
            zero.append((_, i))
    board.append(tmp)

dfs(0)