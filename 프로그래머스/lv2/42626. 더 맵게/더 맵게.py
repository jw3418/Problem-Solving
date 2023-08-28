import heapq

def solution(scoville, K):
    N = len(scoville)
    
    heap = []
    for i in range(N):
        heapq.heappush(heap, scoville[i])
    
    count = 0
    while True:
        first = heapq.heappop(heap); second = heapq.heappop(heap)
        
        if first >= K: return count
        if len(heap) <= 0:
            if first + (second*2) >= K:
                return count+1
            return -1
               
        heapq.heappush(heap, first + (second*2))
        count += 1