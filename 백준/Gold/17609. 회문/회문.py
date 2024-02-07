import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    test = sys.stdin.readline().strip()

    left = 0; right = len(test)-1; answer = 0
    while left < right:
        if test[left] == test[right]: left+=1; right-=1; continue
        if test[left] == test[right-1]:
            test_t = test[left:right]
            if test_t[:] == test_t[::-1]: answer=1; break
        if test[left+1] == test[right]:
            test_t = test[left+1:right+1]
            if test_t[:] == test_t[::-1]: answer=1; break
        answer=2; break
    print(answer)