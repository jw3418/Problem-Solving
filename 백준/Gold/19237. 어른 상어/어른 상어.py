import sys

dx = (-1, 1, 0, 0); dy = (0, 0, -1, 1)

N, M, k = map(int, sys.stdin.readline()[:-1].split())

board = [] #[번호, 냄새 count]
for n in range(N): board.append(list(map(int, sys.stdin.readline()[:-1].split())))
for i in range(N):
    for j in range(N):
        if board[i][j] != 0: board[i][j] = [board[i][j], k]

direction = dict(); tmp = list(map(int, sys.stdin.readline()[:-1].split()))
for m in range(M): direction[m+1] = tmp[m]

priority = dict() #상어번호: [(), (), (), ()]
for m in range(1, M+1):
    tmp = []
    for i in range(4): tmp.append(tuple(map(int, sys.stdin.readline()[:-1].split())))
    priority[m] = tmp

answer = 0
while True:
    if answer > 1000: print(-1); exit()
    if len(direction) == 1: print(answer); break

    ##### 인접한 칸으로 이동 1)아무 냄새가 없는 칸으로 2)없으면 자신의 냄새가 있는 칸으로
    next_number = dict(); next_dir = dict()
    for x in range(N):
        for y in range(N):
            if board[x][y] and board[x][y][1] == k:
                number, count = board[x][y]
                curr_dir = direction[number]; curr_pri = priority[number][curr_dir-1]

                candi_empty = []; candi_full = []
                for i in range(4):
                    nx = x + dx[i]; ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] == 0: candi_empty.append((curr_pri.index(i+1), i))
                        elif board[nx][ny][0] == number: candi_full.append((curr_pri.index(i+1), i))
                
                if candi_empty:
                    candi_empty.sort(); i = candi_empty[0][1]
                    nx = x + dx[i]; ny = y + dy[i]
                    if (nx, ny) not in next_number: next_number[(nx, ny)] = [number]
                    else: next_number[(nx, ny)].append(number)
                    next_dir[number] = i+1
                else:
                    candi_full.sort(); i = candi_full[0][1]
                    nx = x + dx[i]; ny = y + dy[i]
                    if (nx, ny) not in next_number: next_number[(nx, ny)] = [number]
                    else: next_number[(nx, ny)].append(number)
                    next_dir[number] = i+1

    ##### 상어가 겹치는 경우 내쫓기 + 자신의 위치에 냄새 뿌리기
    check = set(next_number.keys())

    for npos, numbers in next_number.items():
        if len(numbers) >= 2:
            survived = min(numbers); sidx = numbers.index(survived); numbers.pop(sidx)
            for n in numbers:
                del direction[n]
            direction[survived] = next_dir[survived]
            board[npos[0]][npos[1]] = [survived, k]
        else:
            number = numbers[0]
            direction[number] = next_dir[number]
            board[npos[0]][npos[1]] = [number, k]

    ##### 냄새 count 업데이트 (k가 아닌 냄새 -1, 만약 0이 된다면 list없애고 0으로 갱신)
    for i in range(N):
        for j in range(N):
            if (i, j) not in check and board[i][j] != 0:
                board[i][j][1] -= 1
                if board[i][j][1] == 0: board[i][j] = 0

    answer += 1