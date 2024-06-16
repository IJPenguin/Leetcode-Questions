nums = [1,2,3]
target = 4
memoise = {}
def combinationSum(sum, ind):
    if sum == target:
        return 1 
    if sum > target:
        return 0
    if (sum, ind) in memoise:
        return memoise[(sum, ind)]
    count = 0
    for i in range(len(nums)):
        count += combinationSum(sum + nums[i], i)
    memoise[(sum, ind)] = count
    return count

print(combinationSum(0, 0))