import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input()); note1 = list(map(int, input().split())); note1 = list(set(note1)); N = len(note1)
    M = int(input()); note2 = list(map(int, input().split()))

    note1.sort()
    for target in note2:
        l, r = 0, N-1
        flag = False
        while l<=r:
            mid = (l+r)//2
            if note1[mid] == target:
                flag = True
                break
            else:
                if note1[mid] > target: r = mid-1
                else: l = mid+1
        if flag: print(1)
        else: print(0)