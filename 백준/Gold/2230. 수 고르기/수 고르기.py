import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for n in range(N)]
A.sort()

min_ = int(10e9)
l, r = 0, 0
while r < N and l <= r:
    diff = A[r]-A[l]
    if diff >= M:
        min_ = min(min_, diff)
        l += 1
    else:
        r += 1
print(min_)