import sys

N = int(sys.stdin.readline().strip())
buildings = list(map(int, sys.stdin.readline().strip().split()))

def slope(x1, y1, x2, y2):
    return (y2-y1) / (x2-x1)

answer = 0
for idx, height in enumerate(buildings):
    local = 0

    lmax_ = float('inf')
    for i in range(idx-1, -1, -1): #왼쪽 탐색
        s = slope(idx+1, height, i+1, buildings[i])
        if s < lmax_:
            lmax_ = s
            local += 1

    rmax_ = -float('inf')
    for i in range(idx+1, N):
        s = slope(idx+1, height, i+1, buildings[i])
        if s > rmax_:
            rmax_ = s
            local += 1
    
    answer = max(answer, local)
print(answer)