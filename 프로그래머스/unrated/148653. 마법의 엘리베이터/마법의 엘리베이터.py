def solution(storey):
    
    count = 0
    while storey > 0:
        remainder = storey % 10
        
        if remainder > 5: #올림
            count += 10 - remainder
            storey += 10
            
        elif remainder <= 5: #내림
            count += remainder
            
            if remainder == 5: # remainder가 5라면 다음 자릿수를 기준으로 올릴지 내릴지 정해야함
                next_remainder = (storey//10)%10 #0~4라면 내림 5~9라면 올림
                if next_remainder > 4:
                    storey += 10
        
        storey //= 10 #자릿수를 줄여나감
        
    return count