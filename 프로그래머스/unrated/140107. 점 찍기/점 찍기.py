from math import sqrt

def solution(k, d):
    
    count = 0
    for x in range(0, d+1, k):
        count += (int(sqrt(abs(d**2 - x**2))) // k) + 1
    return count    