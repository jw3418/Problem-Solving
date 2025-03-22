def solution(number, k):
    N = len(number); number = list(map(int, number))
    
    stack = []
    for i in range(N):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
        # print(stack)
    return "".join(map(str, stack[:len(stack)-k]))