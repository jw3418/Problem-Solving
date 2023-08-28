import sys
from collections import deque


green = [[0] * 4 for _ in range(10)]
blue = [[0] * 10 for _ in range(4)]

def move_green(t, x, y):
    if t == 1:
        while True:
            if x >= 10:
                green[x-1][y] = 1
                break
            if green[x][y] != 0:
                green[x-1][y] = 1
                break
            x += 1
    elif t == 2:
        while True:
            if x >= 10:
                green[x-1][y] = 1; green[x-1][y+1] = 1
                break
            if green[x][y] != 0 or green[x][y+1] != 0:
                green[x-1][y] = 1; green[x-1][y+1] = 1
                break
            x += 1
    elif t == 3:
        while True:
            if x >= 10:
                green[x-1][y] = 1; green[x-2][y] = 1
                break
            if green[x][y] != 0:
                green[x-1][y] = 1; green[x-2][y] = 1
                break
            x += 1

def move_blue(t, x, y):
    if t == 1:
        while True:
            if y >= 10:
                blue[x][y-1] = 1
                break
            if blue[x][y] != 0:
                blue[x][y-1] = 1
                break
            y += 1
    elif t == 2:
        while True:
            if y >= 10:
                blue[x][y-1] = 1; blue[x][y-2] = 1
                break
            if blue[x][y] != 0:
                blue[x][y-1] = 1; blue[x][y-2] = 1
                break
            y += 1
    elif t == 3:
        while True:
            if y >= 10:
                blue[x][y-1] = 1; blue[x+1][y-1] = 1
                break
            if blue[x][y] != 0 or blue[x+1][y] != 0:
                blue[x][y-1] = 1; blue[x+1][y-1] = 1
                break
            y += 1


N = int(sys.stdin.readline()[:-1])
cmd = []
for n in range(N):
    t, x, y = map(int, sys.stdin.readline()[:-1].split())
    cmd.append((t, x, y))

total_score = 0
for n in range(N):
    t, x, y = cmd[n]

    ##### 초록색 판 이동
    move_green(t, x, y)

    ##### 초록색 판 점수 획득 + 행 제거
    removed_green = []
    for i in range(10):
        if sum(green[i]) == 4:
            removed_green.append(i)
            total_score += 1
    
    for row in removed_green:
        for i in range(row, 4, -1):
            green[i] = green[i-1]
        green[4] = [0, 0, 0, 0]
    
    ##### 초록색 연한 칸 확인 + 행 제거
    row_cnt = 0
    for i in range(4, 6):
        if sum(green[i]) != 0:
            row_cnt += 1
    
    for _ in range(row_cnt):
        for i in range(10-1, 4, -1):
            green[i] = green[i-1]
        green[4] = [0, 0, 0, 0]
            
    ##### 파란색 판 이동
    move_blue(t, x, y)

    ##### 파란색 판 점수 획득 + 열 제거
    removed_blue = []
    for j in range(6, 10):
        tmp = 0
        for i in range(4):
            tmp += blue[i][j]
        if tmp == 4:
            removed_blue.append(j)
            total_score += 1
    
    for col in removed_blue:
        for j in range(col, 4, -1):
            for i in range(4):
                blue[i][j] = blue[i][j-1]
        for i in range(4):
            blue[i][4] = 0

    ##### 파란색 연한 칸 확인 + 열 제거
    col_cnt = 0
    for j in range(4, 6):
        for i in range(4):
            if blue[i][j] != 0:
                col_cnt += 1
                break
    
    for _ in range(col_cnt):
        for j in range(10-1, 4, -1):
            for i in range(4):
                blue[i][j] = blue[i][j-1]
        for i in range(4):
            blue[i][4] = 0


print(total_score)
result = 0
for i in range(6, 10):
    result += sum(green[i])
for i in range(4):
    for j in range(6, 10):
        result += blue[i][j]
print(result)