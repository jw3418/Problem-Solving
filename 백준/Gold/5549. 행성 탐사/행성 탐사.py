import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())
board = [list(input().strip()) for m in range(M)]
rect = [list(map(int, input().split())) for k in range(K)]

J = [[0]*(N+1) for m in range(M+1)]
O = [[0]*(N+1) for m in range(M+1)]
I = [[0]*(N+1) for m in range(M+1)]

for i in range(M):
    for j in range(N):
        J[i+1][j+1] = J[i+1][j] + J[i][j+1] - J[i][j]
        O[i+1][j+1] = O[i+1][j] + O[i][j+1] - O[i][j]
        I[i+1][j+1] = I[i+1][j] + I[i][j+1] - I[i][j]

        if board[i][j] == 'J': J[i+1][j+1] += 1
        elif board[i][j] == 'O': O[i+1][j+1] += 1
        elif board[i][j] == 'I': I[i+1][j+1] += 1

for a, b, c, d in rect:
    print(J[c][d] - J[a-1][d] - J[c][b-1] + J[a-1][b-1], end=" ")
    print(O[c][d] - O[a-1][d] - O[c][b-1] + O[a-1][b-1], end=" ")
    print(I[c][d] - I[a-1][d] - I[c][b-1] + I[a-1][b-1])
