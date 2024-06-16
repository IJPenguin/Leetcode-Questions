# nums = [7,4,3,9,1,8,5,2,6]
nums = [40527,53696,10730,66491,62141,83909,78635,18560]
mem = []
k = 2

result = []

def memoisednum(nums, mem , k , i):
    # add the k-1 and append into arr
    if len(mem) == 0:
        num = sum(nums[i - k + 1: i + k + 1])
        mem.append(num)
        return num + nums[i-k]
    else:
        num = mem[-1] + nums[i + k] - nums[i - k]
        mem.append(num)
        return num + nums[i - k]


for i in range(len(nums)):
    if i < k or i > len(nums) - k - 1:
        result.append(-1)
    else:
        num = memoisednum(nums, mem , k , i)// (2 * k + 1)
        result.append(num)

print(result)
