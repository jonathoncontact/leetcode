

def containsDuplicate(nums):
    seen = set() # Use a set to keep track of seen
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

nums = [1, 2, 3, 4, 1]
result = containsDuplicate(nums)
print(result)