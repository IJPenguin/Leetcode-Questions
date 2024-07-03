def productExceptSelf(nums):
    prefix = 1
    n = len(nums)
    res = [1] * n
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))