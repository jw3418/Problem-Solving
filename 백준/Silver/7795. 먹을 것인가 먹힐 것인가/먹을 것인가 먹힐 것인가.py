import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(); B.sort()
    # 1 1 3 7 8
    # 1 3 6
    cnt = 0; a = 0
    for b in range(M):
        while a < N:
            if B[b] < A[a]:
                cnt += N-a
                break
            else:
                a += 1
    print(cnt)