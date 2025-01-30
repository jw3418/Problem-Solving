import sys
input = sys.stdin.readline

N = int(input())
L = [int(input()) for n in range(N)]
P = [0] * (N+1) # 거리배열을 위치배열(prefix_sum)으로 바꿔줌
for i in range(N):
    P[i+1] = P[i] + L[i]

total = P[-1]
l, r = 0, 0
max_ = 0
while l < N and r < N:
    dist = min(P[r]-P[l], total-(P[r]-P[l]))
    if dist > max_: max_ = dist
    
    if P[r]-P[l] < total-(P[r]-P[l]):
        r += 1
    else:
        l += 1
print(max_)