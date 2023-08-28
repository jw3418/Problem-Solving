import sys
from collections import deque

n = int(input())
S = deque(list(sys.stdin.readline()[:-1]))
Matrix = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(-1)
    Matrix.append(tmp)
for i in range(n):
    for j in range(i, n):
        Matrix[i][j] = S.popleft()
visit = []

def satisfy(sign, num):
    if sign == '-' and num < 0:
        return True
    elif sign == '+' and num > 0:
        return True
    elif sign == '0' and num == 0:
        return True
    else:
        return False

def dfs(depth):
    if depth == n:
        print(" ".join(map(str, visit)))
        only_one_flag = 1
        exit(0) #process 종료
    for i in range(-10, 11):
        if satisfy(Matrix[depth][depth], i):
                visit.append(i)

                s = 0; err = 0
                for x in range(depth, -1, -1):
                    s += visit[x]
                    if not satisfy(Matrix[x][depth], s):
                        err = 1; break

                if err == 0:
                    dfs(depth+1)

                visit.pop()
            
dfs(0)