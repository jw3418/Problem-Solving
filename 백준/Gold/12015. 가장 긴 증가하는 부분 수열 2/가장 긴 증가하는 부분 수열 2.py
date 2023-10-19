import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))

LIS = [-1]
for a in A:
    if LIS[-1] < a:
        LIS.append(a)
    else: #이분 탐색을 통해 a가 들어가 위치를 찾음
        left = 0
        right = len(LIS)

        while left < right:
            mid = (left+right)//2
            if LIS[mid] < a: left = mid+1
            else: right = mid
        LIS[right] = a
print(len(LIS)-1)