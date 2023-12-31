import sys
sys.setrecursionlimit(10**6)

pre = []
while True:
    try: pre.append(int(sys.stdin.readline().strip()))
    except: break

def post(start, end):
    if start > end: return

    mid = end+1
    for i in range(start+1, end+1):
        if pre[start] < pre[i]:
            mid = i; break
    
    post(start+1, mid-1)
    post(mid, end)
    print(pre[start])

post(0, len(pre)-1)