nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

def longestConsecutive(nums) -> int:
    if not nums:
        return 0
    nums = list(set(nums))
    res = 1
    for num in nums:
        if num - 1 not in nums:
            cur_el = num
            cur = 1
            while cur_el + 1 in nums:
                cur_el += 1
                cur += 1
            res = max(cur, res)
    return res
print(longestConsecutive(nums))