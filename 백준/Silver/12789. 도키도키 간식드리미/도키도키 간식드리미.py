import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))

Sort_T = sorted(T, reverse=True)
stack = []
for t in T:
    if Sort_T[-1] == t:
        Sort_T.pop()
    else:
        while stack and stack[-1] == Sort_T[-1]:
            Sort_T.pop(); stack.pop()
        stack.append(t)
    # print("Sort_T = ", Sort_T)
    # print("stack = ", stack)
if Sort_T == stack: print("Nice")
else: print("Sad")


'''
4 2 1 3

4
4 2
4
'''