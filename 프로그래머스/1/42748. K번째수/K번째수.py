def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        tmp = array[i-1:j]; k -= 1
        tmp.sort(); answer.append(tmp[k])
        
    return answer