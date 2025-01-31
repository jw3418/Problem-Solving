import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    H = list(map(int, input().split()))
    P = [0] * (N+M)
    for i in range(N+M-1): P[i+1] = P[i] + H[i%N]
    # print(P)

    if N == M:
        if sum(H) < K: print(1)
        else: print(0)
    else:
        cnt = 0
        for i in range(len(P)-M):
            sum_ = P[i+M] - P[i]
            if sum_ < K: cnt += 1
        print(cnt)

'''
1
8 3 15
3 4 7 5 6 4 2 9

1
5 5 16
1 2 3 4 5
'''