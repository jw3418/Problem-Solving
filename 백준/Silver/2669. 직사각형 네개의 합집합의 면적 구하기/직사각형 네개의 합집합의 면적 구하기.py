import sys
input = sys.stdin.readline

rect = [list(map(int, input().split())) for i in range(4)]
board = [[0]*100 for _ in range(100)]
for r in rect:
    r[0]-=1; r[1]-=1; r[2]-=1; r[3]-=1
    for i in range(r[0], r[2]):
        for j in range(r[1], r[3]):
            board[i][j] = 1
ans = 0
for i in range(100): ans += sum(board[i])
print(ans)