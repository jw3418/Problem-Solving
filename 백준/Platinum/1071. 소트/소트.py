from collections import Counter

def insert_numbers(index):
    global a_len
    while count[index]:
        ans.append(index)
        count[index] -= 1
        a_len -= 1

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
a_len = n
sorted_numbers = sorted(count)
ans = []

while a_len > 0:
    for k in range(len(sorted_numbers)):
        flag = True
        i = sorted_numbers[k]
        if count[i] != 0:
            if i + 1 in sorted_numbers and count[i + 1] != 0:
                for j in sorted_numbers[k + 1:]:
                    if i + 2 <= j and count[j] != 0:
                        insert_numbers(i)
                        ans.append(j)
                        count[j] -= 1
                        a_len -= 1
                        flag = False
                        break
                if flag:
                    ans.append(i + 1)
                    count[i + 1] -= 1
                    a_len -= 1
            else:
                insert_numbers(i)

print(*ans)
