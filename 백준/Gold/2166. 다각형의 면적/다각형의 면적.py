import sys

N = int(sys.stdin.readline().strip())
coor = [list(map(int, sys.stdin.readline().strip().split())) for n in range(N)]; coor.append(coor[0])

sum_1, sum_2 = 0, 0
for n in range(N):
    sum_1 += coor[n][0] * coor[n+1][1]
    sum_2 += coor[n][1] * coor[n+1][0]
answer = abs(sum_1 - sum_2) / 2
print(round(answer, 1))