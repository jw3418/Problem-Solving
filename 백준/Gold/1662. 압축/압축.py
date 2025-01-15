import sys
import copy
input = sys.stdin.readline

S = list(input().strip())

stack = []; len_ = 0; prev = 0
for s in S:
    if s == '(':
        stack.append((len_-1, prev))
        len_ = 0
    elif s == ')':
        plen_, weight = stack.pop()
        len_ = len_*weight + plen_
    else:
        len_ += 1
        prev = int(s)
print(len_)

# 10342(76)
# 10347676

# 33(562(71(9)))
# 33(562(79))
# 33(567979)
# 3567979567979567979