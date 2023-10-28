import sys
import heapq

N, K = map(int, sys.stdin.readline().strip().split())
jewels = []
for n in range(N): heapq.heappush(jewels, list(map(int, sys.stdin.readline().strip().split())))
bags = []
for k in range(K): bags.append(int(sys.stdin.readline().strip()))
bags.sort()

answer = 0
candi = []
for bag in bags: #가방을 순회
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(candi, -jewels[0][1]) #가격에 대해 최대힙
        heapq.heappop(jewels)
    if candi: answer -= heapq.heappop(candi)
print(answer)