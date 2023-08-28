import math

def solution(arrayA, arrayB):
    N = len(arrayA)
    
    gcdA = 0; gcdB = 0
    for i in range(N):
        gcdA = math.gcd(gcdA, arrayA[i]); gcdB = math.gcd(gcdB, arrayB[i])

    flagA = True; flagB = True
    for i in range(N):
        if arrayB[i] % gcdA == 0: flagA = False
        if arrayA[i] % gcdB == 0: flagB = False
        if not flagA and not flagB: return 0
    
    if flagA and flagB: return max(gcdA, gcdB)
    elif flagA: return gcdA
    elif flagB: return gcdB