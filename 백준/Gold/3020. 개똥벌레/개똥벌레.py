import sys
from collections import deque
input = sys.stdin.readline

N, H = map(int, input().split())
D = [0]*(H+1)
U = [0]*(H+1)
for n in range(N):
    if n % 2 == 0: D[int(input())] += 1
    else: U[int(input())] += 1

for h in range(H-1, 0, -1): #누적합 구하기
    D[h] += D[h+1]
    U[h] += U[h+1]

min_ = int(10e9)
cnt = 0
for h in range(1, H+1):
    tmp = D[h] + U[H-h+1]
    if min_ > tmp:
        min_ = tmp; cnt = 1
    elif min_ == tmp:
        cnt += 1
print(min_, cnt)