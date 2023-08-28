import sys

tmp = list(map(int, sys.stdin.readline()[:-1].split(' ')))
N = tmp[0]; M = tmp[1]
P = []
for _ in range(N):
    P.append(list(map(int, sys.stdin.readline()[:-1])))

max_value = 0
def bitmask():
    global max_value
    for i in range(1 << N*M):
        local_sum = 0

        for x in range(N):
            x_sum = 0
            for y in range(M):
                idx = x * M + y
                if i & (1 << idx) != 0:
                    x_sum = x_sum * 10 + P[x][y]
                else:
                    local_sum += x_sum; x_sum = 0
            local_sum += x_sum

        for y in range(M):
            y_sum = 0
            for x in range(N):
                idx = x * M + y
                if i & (1 << idx) == 0:
                    y_sum = y_sum * 10 + P[x][y]
                else:
                    local_sum += y_sum; y_sum = 0
            local_sum += y_sum

        max_value = max(max_value, local_sum)

bitmask()
print(max_value)