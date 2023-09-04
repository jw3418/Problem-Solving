import sys


src = sys.stdin.readline()[:-1].split(':')
if src[0] == '':
    src = src[1:]
if src[-1] == '':
    src = src[:-1]

result = ""
for s in src:
    if s == '':
        result += '0000:'*(8-len(src)+1)
    else:
        tmp = s
        for i in range(4 - len(tmp)):
            tmp = '0' + tmp
        result += tmp + ':'
print(result[:-1])