def solution(prices):
    N = len(prices)
    
    result = []
    
    for i in range(N-1):
        cnt = 0
        for j in range(i, N-1):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                break
        result.append(cnt)
    result.append(0)
            
    return result