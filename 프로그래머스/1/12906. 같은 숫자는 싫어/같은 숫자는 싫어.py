def solution(arr):
    stack = []
    for a in arr:
        if stack and stack[-1] == a:
            continue
        else:
            stack.append(a)
    return stack