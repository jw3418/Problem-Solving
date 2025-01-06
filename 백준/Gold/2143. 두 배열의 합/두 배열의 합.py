import sys
import bisect
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ASum = []
for i in range(N):
    for j in range(i, N):
        ASum.append(sum(A[i:j+1]))
BSum = []
for i in range(M):
    for j in range(i, M):
        BSum.append(sum(B[i:j+1]))
ASum.sort(); BSum.sort()

cnt = 0
for i in range(len(ASum)):
    left = bisect.bisect_left(BSum, T - ASum[i])
    right = bisect.bisect_right(BSum, T - ASum[i])
    cnt += right - left
print(cnt)