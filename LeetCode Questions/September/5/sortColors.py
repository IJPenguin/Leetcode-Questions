from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]


nums = [2,0,2,1,1,0]
s = Solution()
s.sortColors(nums)
print(nums)