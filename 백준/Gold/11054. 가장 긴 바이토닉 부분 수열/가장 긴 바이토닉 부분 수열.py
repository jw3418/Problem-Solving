import sys

N = int(input())
A = list(map(int, sys.stdin.readline()[:-1].split(' ')))

dp1 = [0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1

A.reverse()
dp2 = [0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1
dp2.reverse()

tmp = []
for i in range(N):
    tmp.append(dp1[i] + dp2[i])

print(max(tmp) - 1)