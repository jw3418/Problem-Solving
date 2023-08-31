def solution(s):
    
    s = s[2:-2].split('},{')
    
    s_set = []
    for i in range(len(s)):
        s_set.append(list(map(int, s[i].split(','))))
    
    s_set.sort(key=lambda x:len(x))
    
    result = []
    check = set()
    for i in range(len(s_set)):
        for j in range(len(s_set[i])):
            if s_set[i][j] not in check:
                check.add(s_set[i][j])
                result.append(s_set[i][j])
                
    return result