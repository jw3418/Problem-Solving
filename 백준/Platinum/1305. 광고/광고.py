import sys

L = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()
S_len=len(S)
 
table=[0 for _ in range(S_len)]; j = 0
for i in range(1,S_len):
    while j>0 and S[i] != S[j]: j = table[j-1]
    if S[i] == S[j]:
        j += 1; table[i] = j
print(S_len - table[S_len-1])