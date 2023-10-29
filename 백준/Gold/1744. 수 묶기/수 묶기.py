import sys

N = int(sys.stdin.readline().strip())
plus = []; minus = []

answer = 0
for i in range(N):
    num_ = int(sys.stdin.readline().strip())
    if num_ > 1: plus.append(num_)
    elif num_ <= 0: minus.append(num_)
    else: #1은 그냥 더해주기
        answer += num_

plus.sort(reverse=True); minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus): answer += plus[i]
    else: answer += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus): answer += minus[i]
    else: answer += (minus[i] * minus[i+1])

print(answer)