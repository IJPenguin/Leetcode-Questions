# 100277. Minimum Operations to Make Median of Array Equal to K

# You are given an integer array nums and a non-negative integer k. In one operation, you can increase or decrease any element by 1.
# Return the minimum number of operations needed to make the median of nums equal to k.

nums = [2, 5, 6, 8, 5]
nums = sorted(nums)

k = 4

median = 0

def getMedian(nums):
    n = len(nums)
    if n % 2 == 0:
        a = n//2
        b = a + 1
        return (nums[a] + nums[b])//2
    else:
        return nums[n//2 + 1]

while True:
    if median == k:
        break
    