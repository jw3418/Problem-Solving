def solution(elements):
    N = len(elements)

    sum_set = set()
    for i in range(N):
        tmp_sum = elements[i]
        sum_set.add(tmp_sum)
        for j in range(i+1, i+N):
            if j < N:
                tmp_sum += elements[j]
            else:
                tmp_sum += elements[j-N]
            sum_set.add(tmp_sum)
    return len(sum_set)
    
    # sum_set = set();
    # for length in range(1, N+1): #길이가 length인 연속하는 부분 수열의 합
    #     for i in range(N):
    #         tmp_sum = 0
    #         for j in range(i, i+length):
    #             if j < N:
    #                 tmp_sum += elements[j]
    #             else:
    #                 tmp_sum += elements[j-N]
    #         sum_set.add(tmp_sum)
    # return len(sum_set)
        
        