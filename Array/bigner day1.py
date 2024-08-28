nums = [2, 3, 4, 5, 6]
target = 10

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break  
if not any(nums[i] + nums[j] == target for i in range(len(nums)) for j in range(i + 1, len(nums))):
    print("number not found")