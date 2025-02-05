import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))

l = 1; r = max(L)
ans = 0
while l <= r:
    mid = (l + r) // 2

    total = 0
    for x in L:
        if x >= mid: total += (x // mid)
    if total >= M:
        ans = max(ans, mid)
        l = mid + 1
    else:
        r = mid - 1
print(ans)