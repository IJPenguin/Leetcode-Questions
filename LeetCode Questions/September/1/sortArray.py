from typing import List

# Quick Sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        pivot = nums[0]
        l = []
        r = []

        for i in range(1, len(nums)):
            if nums[i] > pivot:
                r.append(nums[i])
            else:
                l.append(nums[i])

        res = self.sortArray(l) + [pivot] + self.sortArray(r)
        return res

# Insertion Sort

# class Solution:
#     def sortArray(self, nums:List[int]) -> List[int]:
#         for j in range(1, len(nums)):
#             key = nums[j]

#             i = j - 1

#             while i >= 0 and nums[i] > key:
#                 nums[i + 1] = nums[i]
#                 i -= 1
#             nums[i + 1] = key
#         return nums

# Merge Sort

# class Solution:
#     def sortArray(self, nums:List[int]) -> List[int]:
        
#         return nums
    
nums = [5,2,3,1]
print(Solution().sortArray(nums))