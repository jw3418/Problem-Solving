answer = 0
def solution(n):
    global answer
    
    def adjacent(r):
        for i in range(r):
            if rows[i] == rows[r] or abs(rows[i] - rows[r]) == r-i: #같은 열이거나 대각선에 있는 경우 False 반환
                return False
        return True
    
    def dfs(depth):
        global answer
        
        if depth == n: # 성공
            answer += 1
            return
        
        for i in range(n):
            rows[depth] = i
            
            for r in range(depth):
                if rows[r] == rows[depth] or abs(rows[r] - rows[depth]) == depth - r:
                    break
            else:
                dfs(depth+1)

    rows = [0] * n #row당 queen의 column 위치
    dfs(0)
    return answer