def solution(s):
    
    stack = []
    for i in range(len(s)):
        if s[i] == '(': stack.append(s[i])
        else:
            if stack: stack.pop()
            else: return False
    if stack: return False
    else: return True