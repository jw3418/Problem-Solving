import sys
import heapq

T = int(sys.stdin.readline()[:-1])
for t in range(T):
    M = int(sys.stdin.readline()[:-1])
    sequence = []
    for _ in range(M//10 + 1):
        sequence.extend(list(map(int, sys.stdin.readline()[:-1].split())))

    max_heap = []; min_heap = []; result = []
    for m in range(M):

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -sequence[m])
        else:
            heapq.heappush(min_heap, sequence[m])
        
        if min_heap:
            if -max_heap[0] > min_heap[0]:
                low = -heapq.heappop(max_heap); high = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -high)
                heapq.heappush(min_heap, low)
        
        if m % 2 == 0:
            result.append(-max_heap[0])

    print(len(result))
    cnt = 0
    for i in range(len(result)):
        if cnt == 10:
            print(); print(result[i], end = " "); cnt = 1
        else:
            print(result[i], end = " "); cnt += 1