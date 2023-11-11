import sys

N = int(sys.stdin.readline().strip()); answer = N
for i in range(N):
    word = sys.stdin.readline().strip()
    for j in range(len(word)-1):
        if word[j] == word[j+1]: continue
        if word[j] in word[j+1:]: answer -= 1; break
print(answer)