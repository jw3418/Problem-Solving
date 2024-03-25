import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
sushi = [int(input()) for n in range(N)]

l, r = 0, 0
type_ = 0
while l <= N-1:
    r = l + K
    tmp = set(); flag = True
    for i in range(l, r):
        i %= N
        tmp.add(sushi[i])

    cnt = len(tmp)
    if C not in tmp: cnt += 1
    type_ = max(type_, cnt)
    l += 1
print(type_)