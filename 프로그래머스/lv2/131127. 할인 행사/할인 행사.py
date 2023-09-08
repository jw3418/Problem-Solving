def solution(want, number, discount):
    
    answer = 0
    for i in range(len(discount)-10+1):
        
        check = dict()
        for w in range(len(want)): check[want[w]] = number[w]
        
        flag = True
        for j in range(i, i+10):
            if discount[j] in check: check[discount[j]] -= 1
            else: flag = False; break

        if flag and list(check.values()).count(0) == len(want): answer += 1 
    return answer