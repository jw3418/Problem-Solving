import sys
from collections import deque
input = sys.stdin.readline

N = int(input()); K = int(input())
cards = [int(input()) for n in range(N)]

def dfs(card_idx):
    global result

    if len(card_idx) == K:
        tmp = ""
        for k in range(K): tmp+=str(cards[card_idx[k]])
        result.add(tmp)
    else:
        for n in range(N):
            if n not in card_idx:
                card_idx.append(n)
                dfs(card_idx)
                card_idx.pop()

result = set()
dfs([])
print(len(result))