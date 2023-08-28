from collections import defaultdict

def solution(weights):
    N = len(weights)
    
    pair = defaultdict(int) #초깃값을 0으로 설정해줌
          
    result = 0
    for w in weights:
        result += pair[w] + pair[w*2] + pair[w/2] + pair[(w*3)/2] + pair[(w*2)/3] + pair[(w*4)/3] + pair[(w*3)/4]
        pair[w] += 1
                
    return result