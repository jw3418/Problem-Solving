import sys
import heapq
input = sys.stdin.readline

N = int(input())
D = int(input()) #다솜이 득표수
if N == 1:
    print(0); exit()

heap = []
for n in range(N-1): heapq.heappush(heap, -int(input()))

ans = 0
while True:
    tmp = -heapq.heappop(heap)
    if tmp >= D:
        ans += 1; D += 1
        heapq.heappush(heap, -(tmp-1))
    else: break
print(ans)