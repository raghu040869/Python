def contains_duplicates(nums):
    nums_set = set(nums)
    return len(nums_set) != len(nums)

nums = [1,2,3,1]
print(contains_duplicates(nums))
nums = [1,2,3,4]
print(contains_duplicates(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicates(nums))
