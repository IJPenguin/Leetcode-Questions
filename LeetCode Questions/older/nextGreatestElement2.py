nums = [1, 2, 1]
# nums = [1, 2, 3, 4, 3]
n = len(nums)
nums = nums * 2
res = [-1] * n * 2
stack = []

for i, num in enumerate(nums):
    while stack and num > nums[stack[-1]]:
        ind = stack.pop()
        res[ind] = num
    stack.append(i)

print(res[:n])