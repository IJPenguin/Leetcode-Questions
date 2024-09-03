import random

nums = []


def generate_nums(nums, length, start, end):
    for i in range(length):
        nums.append(random.randint(start, end))

generate_nums(nums, 100, 1, 100)

print(f"Unsorted : {nums}") 
 
def merge_sort(nums):
    if len(nums) == 2:
        return [min(nums), max(nums)]

    if len(nums) == 1:
        return nums

    n = len(nums)
    left = merge_sort(nums[: n//2])
    right = merge_sort(nums[n//2:])
    i, j, k = 0, 0, 0
    temp = [0] * n

    while k < n:
        if i >= len(left):
            temp[k] = right[j]
            j += 1
        elif j >= len(right):
            temp[k] = left[i]
            i += 1
        else:
            if left[i] <= right[j]:
                temp[k] = left[i]
                i += 1
            else:
                temp[k] = right[j]
                j += 1
        k += 1

    return temp


print(merge_sort(nums))
