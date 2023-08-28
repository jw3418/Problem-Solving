import sys

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

def move_shark(x, y, size):
    S, d = shark[size]

    board[x][y] = 0
    for s in range(S):
        x += dx[d]; y += dy[d]
        if x == -1:
            d = 1; shark[size] = (S, d)
            x += dx[d] * 2
        elif x == R:
            d = 0; shark[size] = (S, d)
            x += dx[d] * 2
        elif y == -1:
            d = 2; shark[size] = (S, d)
            y += dy[d] * 2
        elif y == C:
            d = 3; shark[size] = (S, d)
            y += dy[d] * 2
    
    return (x, y, size)


R, C, M = map(int, sys.stdin.readline()[:-1].split())
board = [[0] * C for _ in range(R)]
shark = dict() #크기 : (속력, 방향)
for m in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline()[:-1].split()); d -= 1; r -= 1; c -= 1
    board[r][c] = z
    shark[z] = (s, d)

total_size = 0
for c in range(C):
    # 현재 열에서 가장 가까운 상어 잡기
    size = -1
    for r in range(R):
        if board[r][c] != 0:
            size = board[r][c]; board[r][c] = 0
            break
    if size != -1:
        total_size += size
        del shark[size]

    # 상어 이동
    dest_sharks = []
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                dest_sharks.append(move_shark(i, j, board[i][j]))

    # 이동 완료 후 잡아먹기
    for x, y, size in dest_sharks:
        if board[x][y] == 0:
            board[x][y] = size
        else:
            if board[x][y] < size:
                del shark[board[x][y]]
                board[x][y] = size
            else:
                del shark[size]
    
print(total_size)