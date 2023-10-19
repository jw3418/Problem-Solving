import sys

N, M, K = map(int, sys.stdin.readline().strip().split())

if N > M*K or N < M+K-1: print(-1); exit()

if K == 1:
    print(" ".join(map(str, [i for i in range(1, M+1)]))); exit()

numbers = [1]*M
D = (N-M)//(K-1); R = (N-M)%(K-1)
for i in range(D):
    numbers[i] = K
if R > 0:
    numbers[D] += R

answer = []
tmp = 0
for number in numbers:
    for i in range(tmp+number, tmp, -1):
        answer.append(i)
    tmp += number
print(" ".join(map(str, answer)))