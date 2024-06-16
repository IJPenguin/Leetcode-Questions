# nums = [-1,1,0,-3,3]
nums = [1,2,3,4]

# if 0 in nums:
#     if nums.count(0) >= 2:
#         print([0 for k in range(len(nums))])
#         exit()
#     for el in nums:
#         if el == 0:
#             continue
#         mul *= el

#     for el in nums:
#         if el == 0:
#             res.append(mul)
#             continue
#         res.append(0)
#     print(res)
#     exit()

# for el in nums:
#     if el == 0:
#         continue
#     mul *= el

# for el in nums:
#     if el == 0:
#         res.append(mul)
#         continue
#     res.append(int(mul/el))

res = [1 for _ in range(len(nums))]

pre = 1
for i in range(len(nums)):
    res[i] = pre
    pre *= nums[i]
post = 1
for i in range(len(nums)-1 , -1, -1):
    res[i] *= post
    post *= nums[i]

print(res)

