from typing import List
# Continuation of sort Array from yesterday as I wasnt able to solve it yesterday 
class Solution:
    def sortArray(self, nums:List[int]) -> List[int]:
        if len(nums) == 2:
            return [min(nums), max(nums)]

        if len(nums) == 1:
            return nums

        n = len(nums)
        left = self.sortArray(nums[: n//2])
        right = self.sortArray(nums[n//2:])
        i, j, k = 0, 0, 0
        temp = [0] * n

        while k < n:
            if i >= len(left):
                temp[k] = right[j]
                j += 1
            elif j >= len(right):
                temp[k] = left[i]
                i += 1
            else:
                if left[i] <= right[j]:
                    temp[k] = left[i]
                    i += 1
                else:
                    temp[k] = right[j]
                    j += 1
            k += 1

        return temp

    