import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

near_value = int(10e9)

l = 0; r = N-1; x = 0; y = 0
while l < r:
    value = A[l] + A[r]

    if abs(value) <= near_value:
        x = A[l]; y = A[r]
        near_value = abs(value)
    
    if value <= 0: l+=1
    else: r-=1
print(x, y)