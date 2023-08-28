def solution(sequence, k):
    
    N = len(sequence)
    part_sum = 0
    end = 0
    
    result = []
    for start in range(N):
        
        while part_sum < k and end < N: # end를 가능한만큼 이동
            part_sum += sequence[end]
            end += 1
        
        if part_sum == k:
            result.append((end - start, start, end-1))
        part_sum -= sequence[start]
    
    result.sort()
    return [result[0][1], result[0][2]]