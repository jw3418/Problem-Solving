import sys
input = sys.stdin.readline

N, K = map(int, input().split())
T = list(map(int, input().split()))
TSum = [0] * (N+1)
for i in range(1, N+1):
    TSum[i] += TSum[i-1] + T[i-1]
ans = -int(10e9)
for i in range(1, N-K+2):
    tmp = TSum[i+K-1] - TSum[i-1]
    ans = max(ans, tmp)
print(ans)