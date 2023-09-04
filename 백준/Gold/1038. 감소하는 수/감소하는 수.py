import sys

def combination(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in combination(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result


N = int(sys.stdin.readline().rstrip())
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = []
for i in range(1, 11):
    for comb in combination(number, i):
        comb.sort(reverse=True)
        comb = list(map(str, comb))
        answer.append(int(''.join(comb)))

answer.sort()
if N >= len(answer):
    print(-1)
else:
    print(answer[N])