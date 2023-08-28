tmp = list(map(int, input().split(' ')))
N = tmp[0]; M = tmp[1]

board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1] #상하좌우

def combination(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in combination(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result

def cpy(list):
    tmp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = list[i][j]
    return tmp

def save(wall):
    bbb = cpy(board)
    for i in range(3):
        bbb[wall[i][0]][wall[i][1]] = 1
        
    while True:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if bbb[i][j] == 2:
                    for d in range(4):
                        x = i + dx[d]; y = j + dy[d]
                        if x >= 0 and x < N and y >= 0 and y < M:
                            if bbb[x][y] == 0:
                                bbb[x][y] = 2; cnt += 1
        if cnt == 0:
            break

    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if bbb[i][j] == 0:
                zero_cnt += 1
    return zero_cnt

walls = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            walls.append((i, j))

all_wall = combination(walls, 3)
answer = 0
for i in range(len(all_wall)):
    local_answer = save(all_wall[i])
    answer = max(answer, local_answer)
print(answer)