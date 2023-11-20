import sys

T = int(input())
for _ in range(T):
    string = sys.stdin.readline().strip()
    answer = string[0] + string[-1]
    print(answer)