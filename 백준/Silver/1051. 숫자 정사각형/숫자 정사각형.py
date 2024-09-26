import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for n in range(N): board.append(list(map(int, list(input().strip()))))

def isExistRect(l):
    for i in range(N-l+1):
        for j in range(M-l+1):
            if board[i][j] == board[i][j+l-1] == board[i+l-1][j] == board[i+l-1][j+l-1]:
                return True
    return False

length = min(N, M)
for l in range(length, 0, -1):
    if isExistRect(l):
        print(l**2)
        break