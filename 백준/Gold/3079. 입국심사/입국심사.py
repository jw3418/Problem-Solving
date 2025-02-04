import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = [int(input()) for n in range(N)]
T.sort()

l = T[0]; r = T[-1] * M
ans = r
while l <= r:
    mid = (l + r) // 2
    total_num = 0

    for t in T:
        total_num += mid // t
    if total_num >= M:
        r = mid - 1
        ans = min(ans, mid)
    else:
        l = mid + 1
print(ans)