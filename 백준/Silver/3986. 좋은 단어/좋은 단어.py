import sys
input = sys.stdin.readline

N = int(input())
words = [list(input().strip()) for n in range(N)]
Cnt = 0
for word in words:
    if len(word)%2 == 0:
        stack = []
        while word:
            tmp = word.pop()
            if stack and stack[-1] == tmp:
                stack.pop()
            else:
                stack.append(tmp)
        if not stack: Cnt += 1
print(Cnt)