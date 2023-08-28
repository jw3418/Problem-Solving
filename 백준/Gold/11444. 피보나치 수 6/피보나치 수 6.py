import sys

def multi(mat1, mat2):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                result[i][j] += mat1[i][z] * mat2[z][j] % 1000000007
    return result

def recursion(a, b):
    if b == 1:
        return a
    else:
        tmp = recursion(a, b // 2)
        if b % 2 == 0:
            return multi(tmp, tmp)
        else:
            return multi(multi(tmp, tmp), a)

N = int(sys.stdin.readline()[:-1])
matrix = [[1, 1], [1, 0]]
result = recursion(matrix, N)
print(result[0][1] % 1000000007)