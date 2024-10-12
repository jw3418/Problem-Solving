import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split())); A.reverse()

    max_ = A[0]
    sum_ = 0
    for i in range(1, N):
        if max_ < A[i]:
            max_ = A[i]
        else:
            sum_ += max_ - A[i]
    print(sum_)