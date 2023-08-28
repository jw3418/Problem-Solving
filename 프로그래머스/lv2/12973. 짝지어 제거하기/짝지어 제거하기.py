def solution(s):

    s = list(s)
    
    after_s = []
    for i in range(len(s)):
        after_s.append(s[i])
        if len(after_s) >= 2:
            if after_s[-1] == after_s[-2]:
                after_s.pop(); after_s.pop()
            
    if after_s: return 0
    else: return 1