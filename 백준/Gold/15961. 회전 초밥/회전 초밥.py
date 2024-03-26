import sys
from collections import defaultdict
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
sushi = [int(input()) for n in range(N)]
sushi += sushi[:K]

l, r = 0, K
sushi_dict = defaultdict(int)
sushi_dict[C] = 1
cnt = 1
for i in range(K):
    if sushi_dict[sushi[i]] == 0: cnt += 1
    sushi_dict[sushi[i]] += 1

result = cnt
while l < N:
    sushi_dict[sushi[l]] -= 1
    if sushi_dict[sushi[l]] == 0: cnt -= 1

    sushi_dict[sushi[r]] += 1
    if sushi_dict[sushi[r]] == 1: cnt += 1

    result = max(result, cnt)
    l += 1; r += 1
print(result)