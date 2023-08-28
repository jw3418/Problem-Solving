import sys
import heapq


N = int(sys.stdin.readline()[:-1])
bundle = []
for n in range(N):
    bundle.append(int(sys.stdin.readline()[:-1]))

heap = []
for n in range(N):
    heapq.heappush(heap, bundle[n])

result = 0
while len(heap) >= 2:
    tmp1 = heapq.heappop(heap); tmp2 = heapq.heappop(heap); tmp3 = tmp1 + tmp2
    result += tmp3
    heapq.heappush(heap, tmp3)

print(result)