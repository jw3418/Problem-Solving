import sys

S = int(sys.stdin.readline().strip())

cnt = 0; sum_ = 0
while True:
    cnt += 1
    sum_ += cnt
    if sum_ > S: break
print(cnt-1)