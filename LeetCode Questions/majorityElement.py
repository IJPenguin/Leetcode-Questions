from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        val = 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                val += 1
            else:
                val -= 1
                if val == 0:
                    major = nums[i]
                    val = 1
        return major


nums = [2, 2, 1, 1, 1, 2]
# nums = [3, 2, 3]
s = Solution()
print(s.majorityElement(nums))
