import sys
import math
input = sys.stdin.readline

N = int(input())

A = [False]*2 + [True]*(N-1)
prime = []
for i in range(2, N+1):
    if A[i]:
        prime.append(i)
        for j in range(2*i, N+1, i):
            A[j] = False

cnt = 0
l, r = 0, 0
while r <= len(prime):
    sum_ = sum(prime[l:r])
    if sum_ == N:
        cnt += 1
        r += 1
    elif sum_ < N:
        r += 1
    else:
        l += 1
print(cnt)