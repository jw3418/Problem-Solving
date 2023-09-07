from collections import deque

def solution(s):
    N = len(s)
    
    answer = 0
    for x in range(N):
        stack = []; pos_flag = True
        for i in range(N):
            if s[i] == ']':
                if stack:
                    if stack.pop() != '[': pos_flag = False; break
                else: pos_flag = False; break
            elif s[i] == '}':
                if stack:
                    if stack.pop() != '{': pos_flag = False; break
                else: pos_flag = False; break
            elif s[i] == ')':
                if stack:
                    if stack.pop() != '(': pos_flag = False; break
                else: pos_flag = False; break
            else:
                stack.append(s[i])
        s = deque(s); s.rotate(-1); s = list(s)
        
        if pos_flag and not stack: answer += 1
        
    return answer