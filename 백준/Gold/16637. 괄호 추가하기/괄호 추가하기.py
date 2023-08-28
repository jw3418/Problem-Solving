import sys

def operation(a, op, b):
    if op == '+': return a+b
    elif op == '-': return a-b
    elif op == '*': return a*b

def dfs(depth, value):
    global max_result

    if depth == N-1:
        max_result = max(max_result, value)
        return

    if depth + 2 < N: #뒤에 괄호가 없어서 앞에서부터 이어서 계산하는 경우
        dfs(depth+2, operation(value, cmd[depth+1], int(cmd[depth+2])))

    if depth + 4 < N: #뒤에 괄호가 있어서 뒤부터 계산하는 경우
        dfs(depth+4, operation(value, cmd[depth+1], operation(int(cmd[depth+2]), cmd[depth+3], int(cmd[depth+4]))))


N = int(sys.stdin.readline()[:-1])
cmd = list(sys.stdin.readline()[:-1])

max_result = -1 * int(10e9)
dfs(0, int(cmd[0]))
print(max_result)