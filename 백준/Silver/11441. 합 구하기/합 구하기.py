import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
ASum = [0] * (N+1)
for i in range(1, N+1):
    ASum[i] += ASum[i-1] + A[i-1]
for m in range(M):
    s, e = map(int, input().split()); s-=1; e-=1
    ans = ASum[e+1] - ASum[s]
    print(ans)