from collections import Counter

def solution(topping):
    A = Counter(topping)
    B = dict()
    
    count = 0
    for tp in topping: #topping의 원소 순서대로 A의 토핑을 하나씩 B에게 넘겨줌
        if tp in B: B[tp] += 1
        else: B[tp] = 1
        
        A[tp] -= 1
        if A[tp] == 0: A.pop(tp)
        
        if len(A) == len(B): count += 1
        
    return count

    '''
    N = len(topping)
    
    count = 0
    for i in range(1, N-1):
        if len(set(list(topping[:i]))) == len(set(list(topping[i:]))): count += 1
    return count
    '''