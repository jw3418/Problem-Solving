import sys
from collections import deque


N = int(input())
src = list(map(int, list(sys.stdin.readline()[:-1]))); src_bu = src.copy()
dest = list(map(int, list(sys.stdin.readline()[:-1])))

# 첫번째 스위치를 누르는 경우
cnt = 0
for i in range(1, N):
    if src_bu[i-1] != dest[i-1]:
        cnt += 1
        src_bu[i] = 1 - src_bu[i]
        src_bu[i-1] = 1 - src_bu[i-1]
        if i != N-1:
            src_bu[i+1] = 1 - src_bu[i+1]

if ''.join(map(str, src_bu)) == ''.join(map(str, dest)):
    print(cnt)
    exit()

# 첫번째 스위치를 누르지 않는 경우
cnt = 1
src[0] = 1 - src[0]; src[1] = 1 - src[1]
for i in range(1, N):
    if src[i-1] != dest[i-1]:
        cnt += 1
        src[i] = 1 - src[i]
        src[i-1] = 1 - src[i-1]
        if i != N-1:
            src[i+1] = 1 - src[i+1]

if ''.join(map(str, src)) == ''.join(map(str, dest)):
    print(cnt)
    exit()

print(-1)