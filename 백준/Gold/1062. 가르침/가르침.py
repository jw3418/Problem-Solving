import sys


def dfs(idx, learn):
    global max_word

    if learn == K-5:
        local_max_word = 0

        for word in words:
            flag = True
            for w in word:
                if not alphabet[ord(w) - ord('a')]:
                    flag = False; break
            if flag:
                local_max_word += 1

        max_word = max(max_word, local_max_word)
        return

    for i in range(idx, 26):
        if not alphabet[i]:
            alphabet[i] = True
            dfs(i, learn + 1)
            alphabet[i] = False

N, K = map(int, sys.stdin.readline()[:-1].split())

if K < 5: print(0); exit()
elif K == 26: print(N); exit()

words = []; alphabet = [False] * 26
for n in range(N):
    tmp = sys.stdin.readline()[:-1]
    tmp = tmp[4:-4]
    words.append(tmp)

for a in ['a', 'n', 't', 'i', 'c']:
    alphabet[ord(a) - ord('a')] = True

max_word = 0
dfs(0, 0)
print(max_word)