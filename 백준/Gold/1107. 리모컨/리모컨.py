import sys

N = int(input()); M = int(input())

err = []
if M != 0:
    err = list(sys.stdin.readline()[:-1].split(' '))

result = abs(N - 100)
for i in range(1000001):
    i_str = str(i)
    for j in range(len(i_str)):
        if i_str[j] in err:
            break
        if j == len(i_str)-1:
            result = min(abs(N - i) + len(i_str), result)

print(result)