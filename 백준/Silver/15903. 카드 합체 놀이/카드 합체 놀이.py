import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
tmp = list(map(int, input().split()))
for t in tmp: heapq.heappush(A, t)

for m in range(M):
    a = heapq.heappop(A); b = heapq.heappop(A)
    heapq.heappush(A, a+b); heapq.heappush(A, a+b)
print(sum(A))