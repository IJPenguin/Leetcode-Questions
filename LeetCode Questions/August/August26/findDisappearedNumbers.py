from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [x + 1 for x in range(len(nums))]
        return set(arr).difference(set(nums))


nums = [4,3,2,7,8,2,3,1]
s = Solution()
print(s.findDisappearedNumbers(nums))