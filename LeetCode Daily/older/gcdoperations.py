from math import gcd

nums = [10, 10, 3, 6, 6, 8, 10, 5, 9, 4, 6, 4]
n = len(nums)

extracted = [0 for _ in range(n*(n-1)//2)]
ex_ind = 0


def remove_elements(arr, exclude):

    return [inner_arr for inner_arr in arr if not (inner_arr[0] in exclude or inner_arr[1] in exclude)]


def pair_extractor(nums, extracted, index, i):
    global ex_ind
    if i == len(nums) - 1:
        return

    if index >= len(nums) - 1:
        extracted[ex_ind] = [nums[i], nums[index]]
        ex_ind += 1
        return

    extracted[ex_ind] = [nums[i], nums[index]]
    ex_ind += 1
    return pair_extractor(nums, extracted, index+1, i)


for i in range(len(nums)):
    pair_extractor(nums, extracted, i + 1, i)

for el in extracted:
    el.append(gcd(el[0], el[1]))

sortarr = list(reversed(sorted(extracted, key=lambda x: x[2])))

maxarr = []
for i in range(len(sortarr)):
    if not len(sortarr):
        break
    maxtrm = sortarr[0]
    maxarr.append(sortarr[0])
    sortarr.remove(sortarr[0])
    sortarr = remove_elements(sortarr, maxtrm)

max_sum = 0
m = len(maxarr)

for i, el in enumerate(maxarr):
    max_sum += el[2] * m
    m -= 1

print(max_sum)

# from math import gcd
# ex_ind = 0

# def remove_elements(arr, exclude):
#     return [inner_arr for inner_arr in arr if not (inner_arr[0] in exclude or inner_arr[1] in exclude)]


# def pair_extractor(nums, extracted, index, i):
#     global ex_ind
#     if i == len(nums) - 1:
#         return

#     if index >= len(nums) - 1:
#         extracted[ex_ind] = [nums[i], nums[index]]
#         ex_ind += 1
#         return

#     extracted[ex_ind] = [nums[i], nums[index]]
#     ex_ind += 1
#     return pair_extractor(nums, extracted, index+1, i)

# def pair_extractor(nums, extracted, i):
#     global ex_ind
#     n = len(nums)

#     if i >= n - 1:
#         return

#     for j in range(i+1, n):
#         extracted[ex_ind] = [nums[i], nums[j]]
#         ex_ind += 1

#     return pair_extractor(nums, extracted, i+1)

# class Solution:
#     def maxScore(self, nums) -> int:
#         n = len(nums)

#         extracted = [0 for _ in range(n*(n-1)//2)]

#         for i in range(len(nums)):
#             pair_extractor(nums, extracted, i)

#         for el in extracted:
#             el.append(gcd(el[0], el[1]))

#         sortarr = list(reversed(sorted(extracted, key=lambda x: x[2])))

#         maxarr = []
#         for i in range(len(sortarr)):
#             if not len(sortarr):
#                 break
#             maxtrm = sortarr[0]
#             maxarr.append(sortarr[0])
#             sortarr.remove(sortarr[0])
#             sortarr = remove_elements(sortarr, maxtrm)

#         max_sum = 0
#         m = len(maxarr)

#         for i , el in enumerate(maxarr):
#             max_sum += el[2] * m
#             m -= 1

#         return max_sum

# sol = Solution()
# print(sol.maxScore([1,2]))
