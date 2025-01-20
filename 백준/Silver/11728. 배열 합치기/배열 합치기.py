import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split())); # B.sort(reverse=True)
res = A+B; res.sort()
print(" ".join(map(str, res)))

# result = []
# for n in range(N):
#     while B and B[-1] < A[n]:
#         result.append(B.pop())
#     result.append(A[n])
# while B: result.append(B.pop())
# print(" ".join(map(str, result)))