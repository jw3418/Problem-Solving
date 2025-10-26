import sys
input = sys.stdin.readline

A, P = map(int, input().split())
visit = dict(); visit[A] = 1

cur = A
while True:
    tmp = cur
    nex = 0
    while tmp != 0:
        nex += (tmp % 10) ** P
        tmp //= 10

    if nex in visit:
        if visit[nex] > 2: break
        else: visit[nex] += 1
    else: visit[nex] = 1

    cur = nex

ans = 0
for key, value in visit.items():
    if value == 1: ans += 1
print(ans)