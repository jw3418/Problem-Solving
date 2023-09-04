import sys

tmp = list(map(int, sys.stdin.readline()[:-1].split(' '))); L = tmp[0]; C = tmp[1]
letter = sys.stdin.readline()[:-1].split(' ')
letter.sort()
visit = []; check = {'a', 'e', 'i', 'o', 'u'}

def dfs(flag):
    if len(visit) == L:
        cnt1 = 0; cnt2 = 0
        for j in range(L):
            if visit[j] in check:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            print("".join(map(str, visit)))
        return
    for i in range(flag, C):
        if letter[i] not in visit:
            visit.append(letter[i])
            dfs(i)
            visit.pop()

dfs(0)