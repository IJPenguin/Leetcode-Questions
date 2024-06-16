nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = []
left = 0
right = len(nums)

while left < right - k + 1:
    maxm = float("-inf")
    for i in range(left, left + k):
        if nums[i] > maxm:
            maxm = nums[i]
    res.append(maxm)
    left += 1

print(res)