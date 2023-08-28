import sys

def backtracking(x, y, count):
    global min_count

    # return 조건
    if y >= 10:
        min_count = min(min_count, count)
        return
    if x >= 10:
        backtracking(0, y+1, count)
        return
    
    if board[x][y] == 1:
        for p in range(1, 6):
            if paper[p] == 5: #해당 색종이를 모두 다 사용한 경우
                continue
            if x + p > 10 or y + p > 10: #범위를 벗어나는 경우
                continue

            possible = True
            for i in range(x, x+p): #색종이를 붙일 수 있는 지 없는 지 판별
                for j in range(y, y+p):
                    if board[i][j] == 0:
                        possible = False; break
                if not possible: break
            
            if possible:
                for i in range(x, x+p): #색종이 붙이기
                    for j in range(y, y+p):
                        board[i][j] = 0
                
                paper[p] += 1
                backtracking(x+p, y, count + 1)
                paper[p] -= 1

                for i in range(x, x+p): #색종이 다시 떼기 (for backtracking)
                    for j in range(y, y+p):
                        board[i][j] = 1
    else:
        backtracking(x+1, y, count)


board = []
for _ in range(10):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))
paper = [0 for _ in range(5 + 1)] #각 종류의 색종이는 5개씩 가지고 있다.

min_count = int(10e9)
backtracking(0, 0, 0)
if min_count == int(10e9): print(-1)
else: print(min_count)