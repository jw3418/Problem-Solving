# https://softeer.ai/practice/info.do?idx=1&eid=392&sw_prbl_sbms_sn=265146

import sys

N = int(sys.stdin.readline()[:-1])
courses = []
for n in range(N):
    start, end = map(int, sys.stdin.readline().split())
    courses.append((start, end))
courses.sort(key=lambda x: (x[1], x[0]))

now = -1; answer = 0
for s, e in courses:
    if s >= now:
        answer += 1
    else: continue
    now = e

print(answer)
