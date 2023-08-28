import sys


green = [[0] * 4 for _ in range(10)]
blue = [[0] * 10 for _ in range(4)]

def move_green(t, x, y):
    if t == 1:
        while True:
            if x >= 10:
                green[x-1][y] = 1; break
            if green[x][y] != 0:
                green[x-1][y] = 1; break
            x += 1
    elif t == 2:
        while True:
            if x >= 10:
                green[x-1][y] = 2; green[x-1][y+1] = 2; break
            if green[x][y] != 0 or green[x][y+1] != 0:
                green[x-1][y] = 2; green[x-1][y+1] = 2; break
            x += 1
    elif t == 3:
        while True:
            if x >= 10:
                green[x-1][y] = 3; green[x-2][y] = 3; break
            if green[x][y] != 0:
                green[x-1][y] = 3; green[x-2][y] = 3; break
            x += 1

def move_blue(t, x, y):
    if t == 1:
        while True:
            if y >= 10:
                blue[x][y-1] = 1; break
            if blue[x][y] != 0:
                blue[x][y-1] = 1; break
            y += 1
    elif t == 2:
        while True:
            if y >= 10:
                blue[x][y-1] = 2; blue[x][y-2] = 2; break
            if blue[x][y] != 0:
                blue[x][y-1] = 2; blue[x][y-2] = 2; break
            y += 1
    elif t == 3:
        while True:
            if y >= 10:
                blue[x][y-1] = 3; blue[x+1][y-1] = 3; break
            if blue[x][y] != 0 or blue[x+1][y] != 0:
                blue[x][y-1] = 3; blue[x+1][y-1] = 3; break
            y += 1

def gravity(color):
    if color == "green":
        for i in range(10-2, 4, -1):
            idx_flag = -1
            for j in range(4):
                if idx_flag == j:
                    continue
                if green[i][j] == 1 or green[i][j] == 3:
                    row = i
                    while True:
                        if 0 <= row+1 < 10 and green[row+1][j] == 0:
                            green[row+1][j] = green[row][j]; green[row][j] = 0
                            row += 1
                        else:
                            break
                elif green[i][j] == 2: 
                    row = i
                    while True:
                        if 0 <= row+1 < 10 and green[row+1][j] == 0 and green[row+1][j+1] == 0:
                            green[row+1][j] = green[row][j]; green[row][j] = 0
                            green[row+1][j+1] = green[row][j+1]; green[row][j+1] = 0
                            row += 1
                        else:
                            break
                    idx_flag = j+1 #다음 열은 pass

    elif color == "blue":
        for j in range(10-2, 4, -1):
            idx_flag = -1
            for i in range(4):
                if idx_flag == i:
                    continue
                if blue[i][j] == 1 or blue[i][j] == 2:
                    col = j
                    while True:
                        if 0 <= col+1 < 10 and blue[i][col+1] == 0:
                            blue[i][col+1] = blue[i][col]; blue[i][col] = 0
                            col += 1
                        else:
                            break
                elif blue[i][j] == 3:
                    col = j
                    while True:
                        if 0 <= col+1 < 10 and blue[i][col+1] == 0 and blue[i+1][col+1] == 0:
                            blue[i][col+1] = blue[i][col]; blue[i][col] = 0
                            blue[i+1][col+1] = blue[i+1][col]; blue[i+1][col] = 0
                            col += 1
                        else:
                            break
                    idx_flag = i+1 #다음 행은 pass

def get_score(color):
    global total_score

    gravity_flag = False
    if color == "green":
        for i in range(10):
            check = 0
            for j in range(4):
                if green[i][j] == 0:
                    break
                check += 1
            if check == 4:
                green[i] = [0, 0, 0, 0]
                total_score += 1
                gravity_flag = True
    elif color == "blue":
        for j in range(6, 10):
            check = 0
            for i in range(4):
                if blue[i][j] == 0:
                    break
                check += 1
            if check == 4:
                for x in range(4):
                    blue[x][j] = 0
                total_score += 1
                gravity_flag = True

    return gravity_flag

def light_check(color):
    if color == "green":
        row_cnt = 0
        for i in range(4, 6):
            if sum(green[i]) != 0:
                row_cnt += 1
        for _ in range(row_cnt):
            for i in range(10-1, 4, -1):
                green[i] = green[i-1]
            green[4] = [0, 0, 0, 0]
    elif color == "blue":
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
    gravity_green_flag = get_score("green")
    # 경계 또는 다른 타일 만날때까지 내려감 (대신 블록 단위로 내려가야함!)
    if gravity_green_flag:
        gravity("green")
    
    ##### 초록색 연한 칸 확인 + 행 제거
    light_check("green")

    ##### 연한 칸 처리 이후 초록색 판 점수 획득 + 행 제거
    gravity_green_flag = get_score("green")
    # 경계 또는 다른 타일 만날때까지 내려감 (대신 블록 단위로 내려가야함!)
    if gravity_green_flag:
        gravity("green")
            
    ##############################################################################

    ##### 파란색 판 이동
    move_blue(t, x, y)

    ##### 파란색 판 점수 획득 + 열 제거
    gravity_blue_flag = get_score("blue")
    # 경계 또는 다른 타일 만날때까지 내려감 (대신 블록 단위로 내려가야함!)
    if gravity_blue_flag:
        gravity("blue")

    ##### 파란색 연한 칸 확인 + 열 제거
    light_check("blue")

    ##### 연한 칸 처리 이후 파란색 판 점수 획득 + 열 제거
    gravity_blue_flag = get_score("blue")
    # 경계 또는 다른 타일 만날때까지 내려감 (대신 블록 단위로 내려가야함!)
    if gravity_blue_flag:
        gravity("blue")

    # print()
    # for x in range(10):
    #     for y in range(4):
    #         print(green[x][y], end=" ")
    #     print()
    # for x in range(4):
    #     for y in range(10):
    #         print(blue[x][y], end=" ")
    #     print()


print(total_score)
count = 0
for i in range(6, 10):
    for j in range(4):
        if green[i][j] != 0: count += 1
for i in range(4):
    for j in range(6, 10):
        if blue[i][j] != 0: count += 1
print(count)