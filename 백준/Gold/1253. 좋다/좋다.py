import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
A.sort()

cnt = 0
for i in range(N):
    A_t = A[:i]+A[i+1:]
    left, right = 0, N-2
    while left < right:
        sum_ = A_t[left] + A_t[right]
        if sum_ == A[i]:
            cnt += 1
            break
        if sum_ < A[i]: left += 1
        else: right -= 1
print(cnt)