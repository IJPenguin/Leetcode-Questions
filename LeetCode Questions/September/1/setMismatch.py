from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        start = 0
        res = [0, 0]
        seen = set()
        for i, num in enumerate(nums):
            start += 1
            if start not in nums:
                res[1] = start
            if num in seen:
                res[0] = num
            else:
                seen.add(num)
        return res

# do this problem with the optimised approach of 2 variables and 1 loop


nums1 = [1, 2, 2, 4]
nums2 = [1, 1]
nums3 = [3, 2, 2]
nums4 = [3, 2, 3, 4, 6, 5]
s = Solution()
print(s.findErrorNums(nums1))
print(s.findErrorNums(nums2))
print(s.findErrorNums(nums3))
print(s.findErrorNums(nums4))
