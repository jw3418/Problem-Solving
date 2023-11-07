import sys
import heapq

N = int(sys.stdin.readline().strip())
course = [list(map(int, sys.stdin.readline().strip().split())) for n in range(N)]; course.sort()

heap = []; heapq.heappush(heap, course[0][1])
for i in range(1, N):
    if course[i][0] < heap[0]: heapq.heappush(heap, course[i][1])
    else:
        heapq.heappop(heap); heapq.heappush(heap, course[i][1])
print(len(heap))