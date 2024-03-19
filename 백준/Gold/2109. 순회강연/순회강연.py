import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for n in range(N)]
arr.sort(key=lambda x: (x[1]))
p_get = []
for ele in arr:
    heapq.heappush(p_get, ele[0])
    if len(p_get) > ele[1]:
        heapq.heappop(p_get)
print(sum(p_get))