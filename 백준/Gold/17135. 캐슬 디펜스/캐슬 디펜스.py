import sys
from itertools import combinations
import copy


N, M, D = map(int, sys.stdin.readline()[:-1].split())
origin_board = []
for n in range(N):
    origin_board.append(list(map(int, sys.stdin.readline()[:-1].split())))

archers = list(combinations([idx for idx in range(M)], 3))

max_dead = 0 #구하고자 하는 값
for archer in archers:

    board = copy.deepcopy(origin_board)
    local_max_dead = 0

    while True:
        #궁수의 공격
        will_death = []
        for arc in archer:
            tmp = []
            for i in range(N-1, -1, -1): #열 거꾸로 순회
                for j in range(M):
                    if board[i][j] == 1 and abs(i - N) + abs(j - arc) <= D:
                        tmp.append((abs(i - N) + abs(j - arc), j, i))
            if tmp:
                tmp.sort()
                will_death.append(tmp[0])
        
        cnt = 0
        for wd in will_death:
            d, j, i = wd
            if board[i][j] == 1:
                board[i][j] = 0
                cnt += 1
        local_max_dead += cnt

        # 적 이동
        for i in range(N-1, 0, -1):
            board[i] = board[i-1]
        board[0] = [0 for _ in range(M)]

        #종료조건 확인
        t = 0
        for i in range(N):
            t += sum(board[i])
        if t == 0:
            break


    max_dead = max(max_dead, local_max_dead)

print(max_dead)