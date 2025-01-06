import sys
input = sys.stdin.readline

N, X = map(int, input().split())
li = list(map(int, input().split()))
Sli = [0] * (N+1)
for i in range(1, N+1): Sli[i] += Sli[i-1] + li[i-1]
res = []
for i in range(1, N-X+2): res.append(Sli[i+X-1] - Sli[i-1])
max_ = max(res); cnt = 0
if max_ == 0:
    print("SAD")
    exit()
for i in range(len(res)):
    if res[i] == max_: cnt += 1
print(max_); print(cnt)