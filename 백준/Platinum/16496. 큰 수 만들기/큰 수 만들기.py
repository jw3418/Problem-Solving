import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
greedy = []
for n in nums:
    s = str(n); length = len(s)
    while len(s) < 10: s += s[len(s)-length]
    greedy.append(([*list(s)],str(n)))
greedy.sort(key=lambda x:x[0], reverse=True)

answer = ""
for i in greedy: answer += i[-1]
print(answer if int(answer) != 0 else 0)