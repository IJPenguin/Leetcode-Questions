nums = [2,10,20,19,1]
rep = 0

for i in range(len(nums)-2, -1, -1):
    if nums[i] > nums[i+1]:
        x = nums[i] - nums[i+1]
        nums[i] = nums[i+1]
        nums.insert(i, x)
        rep += 1


print(nums)
print(rep)