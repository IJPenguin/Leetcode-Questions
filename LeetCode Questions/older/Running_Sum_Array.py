nums = [1, 2, 3, 4]
sums = 0
sum_list = []

for num in nums:
    sums += num
    sum_list.append(sums)

# def sum_arr(nums, i , sums):
#     if sums[i]:
#         return sums[i]
    
#     if i <= 0:
#         return nums[0]
    
#     sums[i] = nums[i] + sum_arr(nums, i-1, sums)
#     return sums[i]

# for i in range(len(nums)):
#     sums[i] = sum_arr(nums, i, sums)

print(sums)