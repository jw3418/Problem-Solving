import sys
from collections import Counter

N = int(input())

A = list(map(int, sys.stdin.readline()[:-1].split(' ')))
stack = []; stack.append(0) #stack에는 index를 저장
cnt = Counter(A) #각 인수의 개수를 dictionary 형태로 저장
ans = ['-1' for i in range(N)]

for i in range(1, N):
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        ans[stack.pop()] = str(A[i])
    stack.append(i)

print(' '.join(ans))