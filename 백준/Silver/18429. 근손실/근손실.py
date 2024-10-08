import sys
from itertools import permutations
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
nPr = list(permutations(A, N))
cnt = 0
for i in range(len(nPr)):
    weight = 500
    for n in range(N):
        weight += nPr[i][n]
        weight -= K
        if weight < 500: break
        if n == N-1: cnt += 1
print(cnt)