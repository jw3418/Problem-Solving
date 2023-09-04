import sys

N = int(input())
A = list(map(int, sys.stdin.readline()[:-1].split(' ')))

if N > 1:
    dp1 = [0 for _ in range(N)]; dp1[0] = A[0]
    for i in range(1, N):
        if dp1[i-1] + A[i] < A[i]:
            dp1[i] = A[i]
        else:
            dp1[i] = dp1[i-1] + A[i]

    dp2 = [0 for _ in range(N)]; dp2[0] = A[0]
    for i in range(1, N):
        if dp1[i-1] > dp2[i-1] + A[i]:
            dp2[i] = dp1[i-1]
        else:
            dp2[i] = dp2[i-1] + A[i]

    max_1 = max(dp1); max_2 = max(dp2)
    print(max(max_1, max_2))
else:
    print(A[0])