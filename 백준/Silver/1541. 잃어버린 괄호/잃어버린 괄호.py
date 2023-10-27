import sys

input_ = sys.stdin.readline().strip().split('-')
result = []
for i in range(len(input_)):
    sum_ = 0
    nums = input_[i].split('+')
    for j in range(len(nums)):
        sum_ += int(nums[j])
    result.append(sum_)

answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]
print(answer)