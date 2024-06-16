k = 3
nums = [1, 2, 4, 5]
n = len(nums)
min_diff = float("inf")

for start in range(n):
    and_value = nums[start]
    for end in range(start, n):
        and_value &= nums[end]
        min_diff = min(min_diff, abs(k - and_value))
        if and_value == 0:
            break
