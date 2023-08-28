import sys

def adjacent(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False #열이 같거나, 대각선상에 있으면 False (행-행 == 열-열 인 경우 두 개는 같은 대각선상에 있음)
    return True

def queen(x):
    global result

    if x == N: #N개의 queen을 서로 공격할 수 없게 놓기 성공 
        result += 1
    else:
        for i in range(N): 
            rows[x] = i #x는 행 번호, i는 열 번호
            if adjacent(x): #x 행이 정상적이라면 계속 진행
                queen(x+1)


N = int(input())
rows = [0] * N #row당 queen이 어디에 위치해있는지
result = 0
queen(0)
print(result)