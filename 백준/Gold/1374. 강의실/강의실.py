import sys
import heapq

N = int(sys.stdin.readline().strip())
courses = []
for n in range(N): _, s, e = map(int, sys.stdin.readline().strip().split()); courses.append((s, e))
courses.sort(key=lambda x:x[0])

heap = [] #강의실
answer = 0
for s, e in courses:
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
    answer = max(answer, len(heap))
print(answer)