def solution(clothes):
    dict_ = dict()
    for cloth in clothes:
        if cloth[1] in dict_:
            dict_[cloth[1]] += 1
        else:
            dict_[cloth[1]] = 1
            
    ans = 1
    for key, value in dict_.items():
        ans *= (value+1)
    ans -= 1
    return ans