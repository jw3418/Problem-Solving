from itertools import permutations
import math

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    N = len(numbers); numbers = list(numbers)
    result = set()
    
    for n in range(1, N+1):
        for perm in permutations(numbers, n):
            tmp = int("".join(map(str, list(perm))))
            if tmp > 1 and isPrime(tmp) and tmp not in result: result.add(tmp)
            
    return len(result)