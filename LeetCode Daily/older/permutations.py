nums = [1,2,3]
ans = []

def permutations(nums):
    if len(nums) == 1:
        return [nums]
    else:
        res = []
        for i in range(len(nums)):
            for perm in permutations(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + perm)
    return res

ans = permutations(nums)
print(ans)