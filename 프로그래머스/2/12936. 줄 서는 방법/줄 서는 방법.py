import math

def solution(N, K):
    number = [i for i in range(1, N+1)]
    answer = []
    
    K -= 1
    
    for n in range(N, 0, -1):
        fact = math.factorial(n-1)
        
        idx = K // fact
        answer.append(number.pop(idx))
        
        K %= fact
    
    return answer