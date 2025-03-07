import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

l, r = 0, 0
counter = [0] * (max(A) + 1)
ans = 0
while l <= r and r < N:
    if counter[A[r]] < K:
        counter[A[r]] += 1
        r += 1
    else:
        counter[A[l]] -= 1
        l += 1
    ans = max(ans, r - l)
print(ans)