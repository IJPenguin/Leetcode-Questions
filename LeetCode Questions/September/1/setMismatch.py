from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        start = 0

        for i in range(len(nums)):
            start += 1
            if nums[i] != start:
                return [nums[i], start]


nums1 = [1,2,2,4]
nums2 = [1,1]
nums3 = [3,2,2]
s = Solution()
# print(s.findErrorNums(nums1))
# print(s.findErrorNums(nums2))
print(s.findErrorNums(nums3))