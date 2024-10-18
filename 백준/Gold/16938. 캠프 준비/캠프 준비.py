import sys
from itertools import combinations
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
A = list(map(int, input().split())); A.sort()

cnt = 0
for n in range(2, N+1):
    for li in combinations(A, n):
        if L <= sum(li) <= R:
            if li[-1] - li[0] >= X:
                cnt += 1
print(cnt)
# def dfs(idx_li):
#     if len(idx_li) >= 2:
#         li = []
#         for idx in idx_li: li.append(A[idx])
#         if L <= sum(li) <= R:
#             if li[-1] - li[0] >= X:
#                 result.append(idx_li)
#         return
#     for i in range(N):
#         if i not in idx_li:
#             if not idx_li or i > idx_li[-1]:
#                 dfs(idx_li+[i])

# N, L, R, X = map(int, input().split())
# A = list(map(int, input().split())); A.sort()
# result = []
# dfs([])
# print(result)
# print(len(result))