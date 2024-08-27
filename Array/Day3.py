def threeSum(nums):
    """
    Finds all triplets in the array that sum up to zero.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list represents a triplet.
    """

    nums.sort()  # Sort the array for efficient two-pointer approach
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1

    return result

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
triplets = threeSum(nums)
print(triplets)