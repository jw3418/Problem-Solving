from math import sqrt

def solution(r1, r2):
    max_r = r2
    count = 0
    # x축 기준으로 순회
    for x in range(r1):
        count += int(sqrt(abs(r2**2 - x**2))) - int(sqrt(abs(r1**2 - x**2 - 1)))
    for x in range(r1, r2):
        count += int(sqrt(abs(r2**2 - x**2)))

    return count * 4