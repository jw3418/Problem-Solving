from collections import deque

def solution(n):
    
    ways = 0; local_sum = deque([])
    for i in range(1, n+1):
        local_sum.append(i)
        if sum(list(local_sum)) == n:
            ways += 1
        elif sum(list(local_sum)) > n:
            while sum(list(local_sum)) > n:
                local_sum.popleft()
            if sum(list(local_sum)) == n:
                ways += 1
    return ways