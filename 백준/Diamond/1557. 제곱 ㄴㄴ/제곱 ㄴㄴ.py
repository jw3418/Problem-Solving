def count_square_free_numbers(n):
    p = 0
    for i in range(1, int(n ** 0.5) + 1, 1):
        p += mobius[i] * (n // (i * i))
    return p

left, right = 0, 2000000000
mobius = [0] * 1000001
k = int(input())

mobius[1] = 1

for i in range(1, 1000001):
    if mobius[i]:
        for j in range(i * 2, 1000001, i):
            mobius[j] -= mobius[i]

while left < right - 1:
    mid = (left + right) // 2
    if count_square_free_numbers(mid) < k:
        left = mid
    else:
        right = mid

print(right)
