from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


# next time try to do it in single traversal 

nums1 = [5, 6, 2, 7, 4]
nums2 = [4, 2, 5, 9, 7, 4, 8]
s = Solution()
print(s.maxProductDifference(nums1))
print(s.maxProductDifference(nums2))
