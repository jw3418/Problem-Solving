import sys
input = sys.stdin.readline

N = int(input())
A = []; B = []; C = []; D = []
for n in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

X = dict()
for i in range(N):
    for j in range(N):
        sum_ = A[i] + B[j]
        if sum_ in X: X[sum_] += 1
        else: X[sum_] = 1

ans = 0
for i in range(N):
    for j in range(N):
        sum_ = C[i] + D[j]
        if -sum_ in X: ans += X[-sum_]
print(ans)