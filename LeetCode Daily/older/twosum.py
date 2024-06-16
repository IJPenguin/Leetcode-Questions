nums = [2, 7, 11, 15]
target = 9
ans = []
for num in nums:
    if num > target:
        nums.remove(num)

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            ans.append(i)
            ans.append(j)
