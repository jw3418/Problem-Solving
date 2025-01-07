import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())); A.sort()
X = int(input())

cnt = 0
left, right = 0, N-1
while left < right:
    tmp = A[left] + A[right]
    if tmp == X:
        cnt += 1
        left += 1
    elif tmp < X: left += 1
    else: right -= 1
print(cnt)