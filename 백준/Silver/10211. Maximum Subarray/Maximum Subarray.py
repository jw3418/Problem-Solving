import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    XSum = [0] * (N+1)
    for i in range(1, N+1): XSum[i] = XSum[i-1] + X[i-1]
    
    max_ = -int(10e9)
    for k in range(1, N+1):
        for i in range(1, N-k+2):
            tmp = XSum[i+k-1] - XSum[i-1]
            max_ = max(max_, tmp)
    print(max_)