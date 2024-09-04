from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1
        cur = 1

        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                while num + 1 in nums:
                    num += 1
                    cur += 1
                longest = max(longest, cur)
                cur = 1
        return longest


nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# nums = []
s = Solution()
print(s.longestConsecutive(nums))
