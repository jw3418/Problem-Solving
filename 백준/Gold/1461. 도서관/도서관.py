import sys

N, M = map(int, sys.stdin.readline().strip().split())
A  = list(map(int, sys.stdin.readline().strip().split()))
plus = []; minus = []

max_ = 0
for a in A:
    if a > 0: plus.append(a)
    else: minus.append(a)

    #가장 멀리 있는 책은 마지막에 가져다 놓고 끝내기
    if abs(a) > abs(max_): max_ = a

plus.sort(reverse=True); minus.sort()

answer = 0
for i in range(0, len(plus), M):
    if plus[i] != max_: answer += plus[i]
for i in range(0, len(minus), M):
    if minus[i] != max_: answer += abs(minus[i])
answer *= 2; answer += abs(max_); print(answer)