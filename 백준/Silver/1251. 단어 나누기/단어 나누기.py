import sys
input = sys.stdin.readline

word = list(input().strip())
store = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]; b = word[i:j]; c = word[j:]
        a.reverse(); b.reverse(); c.reverse()
        tmp = a+b+c; tmp = ''.join(tmp)
        store.append(tmp)
store.sort(); print(store[0])