import sys
input = sys.stdin.readline

N = int(input())
S = list(input().strip())
L = len(S)

left, right = 0, 0
max_len = 0
visit = dict(); visit[S[0]] = 1
while right < L and left <= right:
    # print(left, right, visit, end=" ")
    if len(visit) == N:
        max_len = max(max_len, right - left + 1)
        # print(max_len)
        right += 1
        if right < L and S[right] in visit:
            visit[S[right]] += 1
        else:
            right -= 1
            if S[left] in visit:
                if visit[S[left]] == 1: del visit[S[left]]
                else: visit[S[left]] -= 1
            left += 1
    elif len(visit) < N:
        max_len = max(max_len, right - left + 1)
        # print(max_len)
        right += 1
        if right < L:
            if S[right] in visit: visit[S[right]] += 1
            else: visit[S[right]] = 1
print(max_len)