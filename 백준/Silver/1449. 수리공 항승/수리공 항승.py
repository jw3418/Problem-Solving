n,m = map(int,input().split())
pipe = list(map(int,input().split()))
pipe.sort()

S = pipe[0]; cnt = 1

for i in pipe[1:]:
    if (i+0.5)-(S-0.5)<=m:
        continue
    else:
        S = i
        cnt+=1
print(cnt)