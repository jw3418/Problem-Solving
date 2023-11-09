import sys

T = int(sys.stdin.readline().strip())
for t in range(T):
    N = int(sys.stdin.readline().strip())
    numbers = [sys.stdin.readline().strip() for n in range(N)]
    numbers.sort()

    flag = True
    for i in range(N-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]: flag = False; break
    if flag: print('YES')
    else: print('NO')