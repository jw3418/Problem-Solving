import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    S = list(map(int, input().split()))
    S.sort()

    l, r = 0, N-1
    cnt = 0; flag = S[l] + S[r]
    while l < r:
        sum_ = S[l] + S[r]
        if abs(K - sum_) < abs(K - flag):
            flag = sum_
            cnt = 1
        elif abs(K - sum_) == abs(K - flag):
            cnt += 1
        if K < sum_: r -= 1
        else: l += 1
    print(cnt)

'''
1
10 4
-7 9 2 -4 12 1 5 -3 -2 0

-7 -4 -3 -2 0 1 2 5 9 12

1
4 20
1 7 3 5
'''