import sys

N = int(input())
A = list(map(int, sys.stdin.readline()[:-1].split(' ')))

dp = [0 for i in range(N)]
for i in range(0, N): # i가 현재 위치
    for j in range(0, i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

ans = max(dp)
print(ans)

tmp = 0; st = ''
for i in range(N):
    if dp[i] == ans:
        st = str(A[i]); tmp = ans - 1
        for j in range(i - 1, -1, -1):
            if dp[j] == tmp and tmp != 1:
                st = str(A[j]) + ' ' + st; tmp -= 1
            if dp[j] == tmp and tmp == 1:
                st = str(A[j]) + ' ' + st; break
        break

print(st)