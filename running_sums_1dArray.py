def running_sum(nums):
    for i in range (1, len(nums)): 
        nums[i] += nums[i - 1] #i - 1 is why we use i rather than num for the search
    return nums

# Example usage:
nums = [1, 2, 3, 4, 5]
result = running_sum(nums)
print(result)  # Output: [1, 3, 6, 10]