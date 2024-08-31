from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase, decrease = True, True

        for i in range(len(nums) - 1):
            if not nums[i] >= nums[i + 1]:
                increase = False
            if not nums[i] <= nums[i + 1]:
                decrease = False

        return increase or decrease

nums = [1,2,2,3]        
nums = [6,5,4,4]
nums = [1,3,2]
s = Solution()
print(s.isMonotonic(nums)) 