import sys

N, W = map(int, input().split())
weight = []; value = []
for _ in range(N):
    V, C, K = map(int, sys.stdin.readline()[:-1].split()) #V는 물건의 무게, C는 물건의 가치, K는 물건의 개수

    idx = 1 #2의 제곱수
    while K > 0:
        tmp = min(idx, K)
        weight.append(V * tmp)
        value.append(C * tmp)
        idx *= 2
        K -= tmp #이미 계산한 2의 제곱수는 K에서 빼줘야함

dp = [0 for _ in range(W + 1)]
for i in range(len(weight)):
    for j in range(W, 0, -1):
        if j >= weight[i]:
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
print(dp[-1])