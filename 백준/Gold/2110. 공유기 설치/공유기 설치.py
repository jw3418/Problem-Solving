import sys
input = sys.stdin.readline

N, C = map(int, input().strip().split())
loc = [int(input()) for n in range(N)]
loc.sort()

max_ = 0
l_g, r_g = 1, loc[N-1]-loc[0]
while l_g <= r_g:
    gap = (l_g+r_g)//2

    x = loc[0]; cnt = 1
    for i in range(1, N):
        if loc[i] >= x + gap:
            cnt += 1
            x = loc[i]
    
    if cnt >= C:
        max_ = gap
        l_g = gap + 1
    else:
        r_g = gap - 1
print(max_)