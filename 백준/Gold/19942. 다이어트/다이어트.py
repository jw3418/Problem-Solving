import sys
import copy
input = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())
info = [list(map(int, input().split())) for n in range(N)]
result = []

def dfs(sidx):
    global result, min_price

    smp, smf, sms, smv = 0, 0, 0, 0
    lprice = 0
    for i in visit:
        smp += info[i][0]
        smf += info[i][1]
        sms += info[i][2]
        smv += info[i][3]
        lprice += info[i][4]
        if smp >= mp and smf >= mf and sms >= ms and smv >= mv:
            if lprice < min_price:
                min_price = lprice
                result = [i+1 for i in visit]
    
    for i in range(sidx, N):
        if i not in visit:
            visit.append(i)
            dfs(i+1)
            visit.pop()


visit = []
min_price = int(10e9)
dfs(0)
if min_price == int(10e9): print(-1)
else:
    print(min_price)
    print(" ".join(map(str, result)))