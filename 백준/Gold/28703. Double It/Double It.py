import sys
import heapq

N = int(sys.stdin.readline()[:-1])
A = []
mx = 0

for v in map(int, sys.stdin.readline()[:-1].split()):
    mx = max(mx, v)
    heapq.heappush(A, v)

curr_mx = mx
diff = curr_mx - A[0] #현재 최댓값과 최솟값의 차이

while A[0] < mx:
    v = heapq.heappop(A)
    diff = min(diff, curr_mx - v)
    curr_mx = max(curr_mx, 2*v)
    heapq.heappush(A, 2*v)
print(min(curr_mx-A[0], diff))