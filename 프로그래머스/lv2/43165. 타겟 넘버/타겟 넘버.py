from collections import deque

way_cnt = 0
def solution(numbers, target):
    global way_cnt
    N = len(numbers)

    def dfs(operator, depth):
        global way_cnt
        
        if depth == N-1:
            tmp_sum = 0
            for i in range(N):
                if operator[i] == '+':
                    tmp_sum += numbers[i]
                else:
                    tmp_sum -= numbers[i]
            if tmp_sum == target:
                way_cnt += 1
            return
        
        dfs(operator + '+', depth+1)
        dfs(operator + '-', depth+1)
             
    dfs('+', 0)
    dfs('-', 0)
    return way_cnt