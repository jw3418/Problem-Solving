import sys
input = sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def dfs(curr):
    if len(str(curr)) == N:
        print(curr)
    else:
        for i in range(10):
            next = curr*10+i
            if isPrime(next): dfs(next)


N = int(input())
dfs(2); dfs(3); dfs(5); dfs(7)