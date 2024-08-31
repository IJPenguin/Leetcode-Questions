from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        left, right = 0, 0

        for i in range(n):
            leftSum[i] = left
            left += nums[i]

        for i in range(n-1, -1, -1):
            rightSum[i] = right
            right += nums[i]

        for i in range(n):
            if leftSum[i] == rightSum[i]:
                return i
        return -1
    
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = nums[0]
        rightSum = sum(nums) - nums[0]

        if rightSum == 0:
            return 0
        
        for i in range(1, len(nums)):
            rightSum -= nums[i]
            
            if rightSum == leftSum:
                return i

            leftSum += nums[i]

        return -1
            


nums = [1, 7, 3, 6, 5, 6]
s = Solution()
print(s.pivotIndex(nums))
