import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for n in range(N):
    nums = list(map(int, input().split()))
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
print(heap[0])