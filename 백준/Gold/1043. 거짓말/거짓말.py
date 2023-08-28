import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)

    if a in truth and b in truth:
        return
    
    elif a in truth:
        parent[b] = a

    elif b in truth:
        parent[a] = b

    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

N, M = map(int, sys.stdin.readline()[:-1].split())
parent = {i: i for i in range(1, N+1)}
truth = list(map(int, sys.stdin.readline()[:-1].split())); truth = set(truth[1:])

parties = []
for m in range(M):
    party = list(map(int, sys.stdin.readline()[:-1].split()))
    personnel = party[0]; party = party[1:]
    for i in range(personnel - 1):
        union(party[i], party[i+1])

    parties.append(party)

count = 0
for party in parties:
    possible = True
    for i in range(len(party)):
        if find(party[i]) in truth:
            possible = False; break
    if possible: count += 1
print(count)