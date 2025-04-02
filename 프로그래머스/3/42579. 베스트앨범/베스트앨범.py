def solution(genres, plays):
    N = len(genres)
    
    dict_ = dict()
    for i in range(N):
        if genres[i] in dict_:
            dict_[genres[i]].append((plays[i], i))
        else:
            dict_[genres[i]] = [(plays[i], i)]
    
    result = []
    for gen, li in dict_.items():
        li.sort(reverse=True)
        li.sort(key=lambda x:(-x[0], x[1]))
        # print(li)
        sum_ = 0
        for l in li: sum_ += l[0]
        
        tmp = []
        if len(li) < 2:
            tmp.append(sum_); tmp.append(li[0])
        else:
            tmp.append(sum_); tmp.append(li[0]); tmp.append(li[1])    
        result.append(tmp)
    
    result.sort(reverse=True)
    ans = []
    for r in result:
        for i in range(1, len(r)): ans.append(r[i][1])
    return ans