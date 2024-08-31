from typing import List
from collections import Counter
# A pair (i, j) is called good if nums[i] == nums[j] and i < j


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        c = Counter(nums)
        for num, count in c.items():
            res += count * (count - 1) // 2
        return res


nums = [1, 2, 3, 1, 1, 3]
# nums = [1, 1, 1, 1]
# nums = [1, 2, 3]
s = Solution()
print(s.numIdenticalPairs(nums))
