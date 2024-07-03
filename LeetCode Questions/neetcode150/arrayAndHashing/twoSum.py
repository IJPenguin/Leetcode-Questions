def twoSum(nums, target):
    for i, num in enumerate(nums):
        v = target - num
        if v in nums and nums.index(v) != i:
            return [i, nums.index(v)]