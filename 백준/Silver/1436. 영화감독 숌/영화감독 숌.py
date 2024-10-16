import sys
input = sys.stdin.readline

N = int(input())
J = 666
cnt = 0
while True:
    if "666" in str(J):
        cnt += 1
    if cnt == N:
        print(J)
        break
    J += 1