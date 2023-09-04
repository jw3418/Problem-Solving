string1 = input()
string2 = input()
#string1 = "ACAYKP"
#string2 = "CAPCAK"

row = len(string2)
col = len(string1)

table = [[0 for j in range(col+1)] for i in range(row+1)]

for i in range(1, row+1):
    for j in range(1, col+1):
        if string2[i-1] == string1[j-1]: #대각선 왼쪽 위의 값 + 1
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i][j-1], table[i-1][j])

#print(table)
print(table[row][col])