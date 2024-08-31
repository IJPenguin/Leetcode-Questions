from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        for num in nums1:
            pos = nums2.index(num)
            found = False
            for i in range(pos + 1, len(nums2)):
                if nums2[i] > num:
                    res.append(nums2[i])
                    found = True
                    break
            if not found:
                res.append(-1)

        return res

# nums1 = [4,1,2]
# nums2 = [1,3,4,2]        
nums1 = [2,4]
nums2 = [1,2,3,4]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))