import sys
input = sys.stdin.readline

N = int(input()); M = int(input())
A = list(map(int, input().split())); A.sort()
l, r = 0, N-1
cnt = 0
while l < r:
    if A[l] + A[r] == M:
        cnt += 1
        l += 1
    elif A[l] + A[r] < M: l += 1
    else: r -= 1
print(cnt)