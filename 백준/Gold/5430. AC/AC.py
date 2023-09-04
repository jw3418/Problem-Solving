import sys
from collections import deque


T = int(input())
for _ in range(T):
    func = list(sys.stdin.readline()[:-1])
    n = int(sys.stdin.readline()[:-1])
    if n != 0:
        num = deque(list(map(int, sys.stdin.readline()[1:-2].split(','))))
    else:
        tmp = sys.stdin.readline()
        num = deque([])
    error_flag = 0; rev = 0
    for i in range(len(func)):
        if func[i] == 'R':
            rev += 1
        elif func[i] == 'D':
            if len(num) == 0:
                print('error'); error_flag = 1; break
            else:
                if rev % 2 == 0:
                    num.popleft()
                else:
                    num.pop()
    if error_flag == 0:
        if rev % 2 == 0:
            print('[', end='')
            for i in range(len(num)):
                if i == len(num) - 1:
                    print(num[i], end='')
                else:
                    print(num[i], end=',')
            print(']')
        else:
            num.reverse()
            print('[', end='')
            for i in range(len(num)):
                if i == len(num) - 1:
                    print(num[i], end='')
                else:
                    print(num[i], end=',')
            print(']')