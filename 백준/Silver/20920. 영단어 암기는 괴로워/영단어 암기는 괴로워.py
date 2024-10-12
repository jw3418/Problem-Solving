import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
di = dict()
for n in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in di: di[word] += 1
        else: di[word] = 1
heap = []
for word, cnt in di.items(): heapq.heappush(heap, (-cnt, -len(word), word))
# for _, _, ans in heap: print(_, _, ans)
for _ in range(len(heap)):
    _, _, ans = heapq.heappop(heap)
    print(ans)