import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left, right = 0, 0
cnt = 0
visit = [False] * 100001
while left <= right and right < N:
    if not visit[A[right]]:
        visit[A[right]] = True
        right += 1
        cnt += right - left
    else:
        while visit[A[right]]:
            visit[A[left]] = False
            left += 1
print(cnt)