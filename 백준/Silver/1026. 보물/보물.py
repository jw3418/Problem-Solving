import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split())); A.sort()
B = list(map(int, sys.stdin.readline().strip().split())); B.sort(reverse=True)

answer = 0
for i in range(N): answer += A[i] * B[i]
print(answer)