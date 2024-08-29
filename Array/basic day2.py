nums = [1, 2, 3, 4]
running_sum = [nums[0]]

for i in range(1, len(nums)):
  running_sum.append(running_sum[i-1] + nums[i])

print(running_sum)