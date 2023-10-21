import sys

N = int(sys.stdin.readline().strip())
dp_max = [0]*3; dp_min = [0]*3
tmp_max = [0]*3; tmp_min = [0]*3

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    for j in range(3):
        if j == 0:
            tmp_max[j] = a + max(dp_max[j], dp_max[j+1])
            tmp_min[j] = a + min(dp_min[j], dp_min[j+1])
        elif j == 1:
            tmp_max[j] = b + max(dp_max[j-1], dp_max[j], dp_max[j+1])
            tmp_min[j] = b + min(dp_min[j-1], dp_min[j], dp_min[j+1])
        else:
            tmp_max[j] = c + max(dp_max[j], dp_max[j-1])
            tmp_min[j] = c + min(dp_min[j], dp_min[j-1])
    
    for j in range(3):
        dp_max[j] = tmp_max[j]
        dp_min[j] = tmp_min[j]

print(max(dp_max), min(dp_min))