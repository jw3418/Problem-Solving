import sys
import heapq

N = int(sys.stdin.readline()[:-1])
max_heap = [] #중간값보다 작은 값들이 들어감 (가장 큰 값이 가운데이도록 유지)
min_heap = [] #중간값보다 큰 값들이 들어감 (가장 작은 값이 가운데이도록 유지)

for _ in range(N):
    new = int(sys.stdin.readline()[:-1])
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -new)
    else:
        heapq.heappush(min_heap, new)
    
    if min_heap:
        if -max_heap[0] > min_heap[0]:
            low = -heapq.heappop(max_heap); high = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -high)
            heapq.heappush(min_heap, low)

    print(-max_heap[0])