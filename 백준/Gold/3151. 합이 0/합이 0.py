import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())); A.sort()

cnt = 0
for i in range(N-2):
    target = A[i]
    l, r = i+1, N-1
    while l < r:
        sum_ = A[l] + A[r]
        if sum_ + target == 0:
            if A[l] == A[r]: # 합이 0인데 두 수가 같은 경우
                cnt += r - l
                l += 1
            else: #합이 0인데 두 수가 여러개 존재하는 경우
                s, e = l, r
                while A[s] == A[l] and s < r: s += 1
                while A[e] == A[r] and l < e: e -= 1
                cnt += (s-l) * (r-e)
                l, r = s, e
        elif sum_ + target > 0: r -= 1
        else: l += 1
print(cnt)