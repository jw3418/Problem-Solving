import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = []
for n in range(N): array.append(list(map(int, input().split())))

K = int(input())
for k in range(K):
    sx, sy, ex, ey = map(int, input().split())
    sum_ = 0
    for x in range(sx-1, ex):
        for y in range(sy-1, ey):
            sum_ += array[x][y]
    print(sum_)