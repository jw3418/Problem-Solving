import heapq

def solution(jobs):
    N = len(jobs)
    
    idx, cur_time, pre_start = 0, 0, -1
    heap = []
    sum_ = 0
    while idx <= N-1:
        for job in jobs:
            if pre_start < job[0] <= cur_time:
                heapq.heappush(heap, [job[1], job[0]])
        if heap:
            job = heapq.heappop(heap)
            pre_start = cur_time
            cur_time += job[0]
            sum_ += cur_time - job[1]
            idx += 1
        else:
            cur_time += 1
    return sum_ // N