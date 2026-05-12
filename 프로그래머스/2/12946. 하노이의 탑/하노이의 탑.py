def solution(n):
    answer = []
    
    def move(c, l, r, m):
        if c == 1:
            answer.append([l, r])
            return
        move(c-1, l, m, r)
        answer.append([l, r])
        move(c-1, m, r, l)
        
    move(n, 1, 3, 2)
    return answer