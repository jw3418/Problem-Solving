import sys
input = sys.stdin.readline

S = input()
string = set()
for i in range(len(S)):
    for j in range(i+1, len(S)):
        string.add(S[i:j])
print(len(string))