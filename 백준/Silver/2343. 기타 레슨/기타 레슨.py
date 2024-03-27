import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lec = list(map(int, input().split()))

l, r = max(lec), sum(lec)
ans = int(10e9)
while l <= r:
    mid = (l+r)//2 #블루레이의 최대크기

    tmp = 0; cnt = 1
    for i in range(N):
        tmp += lec[i]
        if tmp == mid:
            if i != N-1:
                tmp = 0
                cnt += 1
        elif tmp > mid:
            tmp = lec[i]
            cnt += 1
    
    if cnt <= M:
        ans = min(ans, mid)
        r = mid-1
    elif cnt > M:
        l = mid+1
print(ans)