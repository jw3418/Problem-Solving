def solution(nums):
    N = len(nums)
    s_nums = set(nums)
    type_cnt = len(s_nums)
    
    ans = 0
    if type_cnt <= N//2:
        ans = type_cnt
    else:
        ans = N//2
    return ans