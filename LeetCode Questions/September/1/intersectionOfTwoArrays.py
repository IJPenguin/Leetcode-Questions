from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
        # return [x for x in set(nums1) if x in set(nums2)]


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]

s = Solution()
print(s.intersection(nums1, nums2))
print(s.intersection(nums3, nums4))