import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left, right = 0, N-1
B = A[left] + A[right]
while right < N and left < right:
    tmp = A[left] + A[right]
    if abs(tmp) < abs(B):
        B = tmp
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(B)