import sys

N = int(sys.stdin.readline().strip()); W = list(map(int, sys.stdin.readline().strip().split())); W.sort()

answer = 1
for weight in W:
    if answer < weight: break
    answer += weight
print(answer)