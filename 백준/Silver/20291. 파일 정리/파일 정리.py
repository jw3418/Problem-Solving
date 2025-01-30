import sys
input = sys.stdin.readline

N = int(input())
dict_ = dict()
for n in range(N):
    name, form = map(str, input().strip().split('.'))
    if form in dict_: dict_[form]+=1
    else: dict_[form] = 1
name_ = list(dict_.keys()); name_.sort()
for name in name_: print(name + ' ' + str(dict_[name]))