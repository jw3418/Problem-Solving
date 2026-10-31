def solution(message, spoiler_ranges):
    
    answer = 0
    
    masked = [False] * len(message)
    for sta, end in spoiler_ranges:
        for i in range(sta, end+1):
            masked[i] = True
    
    spoiler = []
    normal = set()
    
    pos = 0
    for word in message.split(' '):
        end = pos + len(word)
        
        if any(masked[pos:end]):
            spoiler.append(word)
        else:
            normal.add(word)
        
        pos = end + 1
    
    visit = set()
    for s in spoiler:
        if s not in visit and s not in normal:
            answer += 1
        visit.add(s)
        
    return answer