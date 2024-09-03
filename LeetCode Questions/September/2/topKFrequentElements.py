from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        temp = list(zip(c.keys(), c.values()))
        return [x for x , y in sorted(temp, reverse=True,  key=lambda x: x[1])[:k]]


nums = [1, 1, 1, 2, 2, 3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
