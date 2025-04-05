import heapq

def solution(operations):
    min_heap = []; max_heap = []
    
    length = 0
    for op in operations:
        op = op.strip().split(" ")
        if op[0] == "I":
            heapq.heappush(min_heap, int(op[1]))
            heapq.heappush(max_heap, -int(op[1]))
            length += 1
        elif op[0] == "D":
            if length > 0:
                if op[1] == '1':
                    min_heap.remove(-heapq.heappop(max_heap))
                else:
                    max_heap.remove(-heapq.heappop(min_heap))
                length -= 1
        if length <= 0:
            min_heap = []; max_heap = []
    
    if length <= 0: return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
