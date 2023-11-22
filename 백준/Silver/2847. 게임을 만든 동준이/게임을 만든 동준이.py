import sys

N = int(sys.stdin.readline().strip())
score = [int(sys.stdin.readline().strip()) for n in range(N)]

answer = 0
for i in range(N-2, -1, -1):
    if score[i] >= score[i+1]: answer += score[i] - score[i+1] + 1; score[i] = score[i+1] - 1
print(answer)