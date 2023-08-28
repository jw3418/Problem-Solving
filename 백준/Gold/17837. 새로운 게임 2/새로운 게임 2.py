import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, K = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))
horses = []; check = [[[] for _ in range(N)] for _ in range(N)]
for k in range(K):
    x, y, direction = map(int, sys.stdin.readline()[:-1].split())
    horses.append([x-1, y-1, direction-1]) #각 말별 정보
    check[x-1][y-1].append(k) #해당위치에 있는 말들의 정보

turn = 0
while True:
    turn += 1
    if turn > 1000:
        print(-1)
        exit()

    for i in range(len(horses)): #0번 말부터 순서대로 이동
        x, y, direction = horses[i]
        nx = x + dx[direction]; ny = y + dy[direction]

        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 0: #흰색
                for start in range(len(check[x][y])):
                    if check[x][y][start] == i:
                        for _ in range(len(check[x][y]) - start):
                            horse_num = check[x][y].pop(start)
                            horses[horse_num][0] = nx; horses[horse_num][1] = ny
                            check[nx][ny].append(horse_num)
                        break

            elif board[nx][ny] == 1: #빨간색
                for start in range(len(check[x][y])):
                    if check[x][y][start] == i:
                        for _ in range(len(check[x][y]) - start):
                            horse_num = check[x][y].pop()
                            horses[horse_num][0] = nx; horses[horse_num][1] = ny
                            check[nx][ny].append(horse_num)
                        break

            elif board[nx][ny] == 2: #파란색
                if direction == 0: direction = 1
                elif direction == 1: direction = 0
                elif direction == 2: direction = 3
                elif direction == 3: direction = 2
                horses[i][2] = direction

                nx = x + dx[direction]; ny = y + dy[direction]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 0: #흰색
                        for start in range(len(check[x][y])):
                            if check[x][y][start] == i:
                                for _ in range(len(check[x][y]) - start):
                                    horse_num = check[x][y].pop(start)
                                    horses[horse_num][0] = nx; horses[horse_num][1] = ny
                                    check[nx][ny].append(horse_num)
                                break

                    elif board[nx][ny] == 1: #빨간색
                        for start in range(len(check[x][y])):
                            if check[x][y][start] == i:
                                for _ in range(len(check[x][y]) - start):
                                    horse_num = check[x][y].pop()
                                    horses[horse_num][0] = nx; horses[horse_num][1] = ny
                                    check[nx][ny].append(horse_num)
                                break
                    elif board[nx][ny] == 2: #파란색
                        nx = x; ny = y
                else: #범위 밖
                    nx = x; ny = y

        else: #범위 밖
            if direction == 0: direction = 1
            elif direction == 1: direction = 0
            elif direction == 2: direction = 3
            elif direction == 3: direction = 2
            horses[i][2] = direction

            nx = x + dx[direction]; ny = y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0: #흰색
                    for start in range(len(check[x][y])):
                        if check[x][y][start] == i:
                            for _ in range(len(check[x][y]) - start):
                                horse_num = check[x][y].pop(start)
                                horses[horse_num][0] = nx; horses[horse_num][1] = ny
                                check[nx][ny].append(horse_num)
                            break

                elif board[nx][ny] == 1: #빨간색
                    for start in range(len(check[x][y])):
                        if check[x][y][start] == i:
                            for _ in range(len(check[x][y]) - start):
                                horse_num = check[x][y].pop()
                                horses[horse_num][0] = nx; horses[horse_num][1] = ny
                                check[nx][ny].append(horse_num)
                            break
                elif board[nx][ny] == 2: #파란색
                    nx = x; ny = y
            else: #범위 밖
                nx = x; ny = y
        
        # 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 바로!!!! 종료
        if len(check[nx][ny]) >= 4:
            print(turn)
            exit()