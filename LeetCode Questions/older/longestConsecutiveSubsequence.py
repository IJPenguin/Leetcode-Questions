# nums = [100, 4, 200, 1,2,3]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]

numSet = set(nums)
l = 0

for el in nums:
    if el -1 in numSet:
        continue
    t = 0
    found = True
    while found:
        if el + t in numSet:
            t += 1
        else:
            found = False
    l = max(t, l)

numSet = set(nums)
l = 1
# memo = {}

# for el in nums:
#     if (el - 1) not in numSet:
#         length = 0
#         while (el + length) in numSet:
#             length += 1
#         l = max(l, length)


print(l)
