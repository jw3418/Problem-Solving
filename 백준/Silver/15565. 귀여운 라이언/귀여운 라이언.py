import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

left, right = 0, 0
ans = int(1e9); cnt = 0
if A[right] == 1: cnt += 1

while right < N and left <= right:
    if cnt == K:
        ans = min(ans, right - left + 1)
        if A[left] == 1: cnt -= 1
        left += 1
    else:
        right += 1
        if right < N and A[right] == 1: cnt += 1
if ans == int(1e9): print(-1)
else: print(ans)