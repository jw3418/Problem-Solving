def solution(begin, end):
    LIMIT = 10000000
    answer = []
    
    for num in range(begin, end+1):
        if num == 1:
            answer.append(0)
            continue
        
        block = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                big = num // i
                small = i
                
                if big <= LIMIT:
                    block = big
                    break

                if small <= LIMIT: #임시
                    block = small 

        answer.append(block)
        
    return answer