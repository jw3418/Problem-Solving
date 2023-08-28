N = int(input())

block = []
for i in range(N):
    block.append(list(map(int, input().split(' '))))

def cpy_block(src_block):
    dest_block = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(src_block[i][j])
        dest_block.append(tmp)
    return dest_block

def move(block, direction):
    if direction == 0: # right
        for i in range(N):
            end = N-1
            for j in range(N-2, -1, -1):
                if block[i][j]:
                    value = block[i][j]
                    block[i][j] = 0
                    if block[i][end] == 0:
                        block[i][end] = value
                    elif block[i][end] == value:
                        block[i][end] = value * 2
                        end -= 1
                    elif block[i][end] != value:
                        end -= 1
                        block[i][end] = value

    elif direction == 1: # left
        for i in range(N):
            end = 0
            for j in range(1, N):
                if block[i][j]:
                    value = block[i][j]
                    block[i][j] = 0
                    if block[i][end] == 0:
                        block[i][end] = value
                    elif block[i][end] == value:
                        block[i][end] = value * 2
                        end += 1
                    elif block[i][end] != value:
                        end += 1
                        block[i][end] = value

    elif direction == 2: # down
        for j in range(N):
            end = N-1
            for i in range(N-2, -1, -1):
                if block[i][j]:
                    value = block[i][j]
                    block[i][j] = 0
                    if block[end][j] == 0:
                        block[end][j] = value
                    elif block[end][j] == value:
                        block[end][j] = value * 2
                        end -= 1
                    elif block[end][j] != value:
                        end -= 1
                        block[end][j] = value

    elif direction == 3: # up
        for j in range(N):
            end = 0
            for i in range(1, N):
                if block[i][j]:
                    value = block[i][j]
                    block[i][j] = 0
                    if block[end][j] == 0:
                        block[end][j] = value
                    elif block[end][j] == value:
                        block[end][j] = value * 2
                        end += 1
                    elif block[end][j] != value:
                        end += 1
                        block[end][j] = value

    return block

def dfs(block, cnt):
    global result
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                result = max(result, block[i][j])
        return
    for i in range(4):
        block_cpyed = cpy_block(block)
        block_moved = move(block_cpyed, i)
        dfs(block_moved, cnt + 1) #recursion을 통한 dfs/ 한 방향 당 탐색 진행

result = 0
dfs(block, 0)
print(result)