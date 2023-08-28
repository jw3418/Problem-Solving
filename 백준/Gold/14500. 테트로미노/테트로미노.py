tmp = list(map(int, input().split(' ')))
N = tmp[0]; M = tmp[1]
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

dshape = [
    [(0, 0), (0, 1), (0, 2), (0, 3)], #1
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)], #2
    [(0, 0), (1, 0), (2, 0), (2, 1)], #3
    [(0, 0), (1, 0), (0, 1), (0, 2)], 
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)], #4
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(1, 0), (2, 0), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)], #5
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
]

def tetris(i, j):
    global result

    for x in range(19):
        local_result = 0
        for y in range(4):
            nx = i + dshape[x][y][0]; ny = j + dshape[x][y][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            local_result += board[nx][ny]
        
        result = max(result, local_result)

result = 0
for i in range(N):
    for j in range(M):
        tetris(i, j)

print(result)