import sys
input = sys.stdin.readline

N = int(input())
di = dict()
for n in range(N):
    book = input().strip()
    if book in di: di[book] += 1
    else: di[book] = 1
res = []; max_ = max(di.values())
for key, value in di.items():
    if value == max_: res.append(key)
res.sort()
print(res[0])