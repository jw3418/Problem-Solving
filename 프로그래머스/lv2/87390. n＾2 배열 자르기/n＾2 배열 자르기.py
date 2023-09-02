def solution(n, left, right):
    
    result = []
    for i in range(left, right+1):
        tmp = max(i%n, i//n) + 1; result.append(tmp)
    return result