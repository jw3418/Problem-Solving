def solution(numbers):
    
    nums = []
    for number in numbers: nums.append(str(number))
    
    #number는 1000이하의 수 -> 3번 이어 붙인 값의 크기 기준 내림차순 정렬
    nums.sort(key=lambda x: list(x*3)[:4], reverse=True)
    
    result = ""
    for num in nums: result += "".join(map(str, num))
    return str(int(result))