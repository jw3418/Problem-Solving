import heapq

def solution(numbers):
    N = len(numbers)
    
    heap = [] # [value, index] 형식
    result = [-1] * N
    
    for i in range(N):
        
        while heap and heap[0][0] < numbers[i]:
            value, index = heapq.heappop(heap)
            result[index] = numbers[i]
            
        heapq.heappush(heap, [numbers[i], i])
        
    return result