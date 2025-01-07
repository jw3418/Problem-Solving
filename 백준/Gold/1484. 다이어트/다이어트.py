import sys
input = sys.stdin.readline

# 4**2 = 16
# 8**2 = 64
# G = 4**2 - 1**2 = 15
# G = 8**2 - 7**2 = 15

G = int(input())
N = 100000
A = [i for i in range(1, N+1)]

result = [] #현재 몸무게 (A[right])
for left in range(N-1):
    right = left + 1; diff = 0
    while diff < G and right < N:
        diff = A[right]**2 - A[left]**2
        right += 1
    if diff == G: result.append(A[right-1])
if len(result) == 0: print(-1)
else:
    result.sort()
    print("\n".join(map(str, result)))