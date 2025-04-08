def solution(answers):
    N = len(answers)
    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    idx1, idx2, idx3 = 0, 0, 0
    sum1, sum2, sum3 = 0, 0, 0
    for answer in answers:
        if answer == one[idx1]: sum1 += 1
        if answer == two[idx2]: sum2 += 1
        if answer == three[idx3]: sum3 += 1
        idx1 += 1; idx1 %= 5
        idx2 += 1; idx2 %= 8
        idx3 += 1; idx3 %= 10
    
    max_ = max(sum1, sum2, sum3)
    result = []
    if sum1 == max_: result.append(1)
    if sum2 == max_: result.append(2)
    if sum3 == max_: result.append(3)
    
    return result