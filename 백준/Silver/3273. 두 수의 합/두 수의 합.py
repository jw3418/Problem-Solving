import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
X = int(input())

A.sort()
cnt = 0
for left in range(N-1):
    right = left + 1; sum_ = 0
    while sum_ < X and left < right < N:
        sum_ = A[left] + A[right]
        right += 1
    if sum_ == X: cnt += 1
print(cnt)