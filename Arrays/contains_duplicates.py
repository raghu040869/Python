def contains_duplicates(nums):
    result = False
    for i in range(len(nums)):
        if nums[i] in nums[i:len(nums) - 1]:
            result = True
            break
    return result

nums = [1, 2, 3, 1]
print(contains_duplicates(nums))
nums = [1,2,3,4]
print(contains_duplicates(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicates(nums))
