from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)
        prev = nums[0]

        for i in range(1, len(nums)):
            l[i] = prev * l[i - 1]
            prev = nums[i]

        prev = nums[-1]
        for i in range(len(nums) - 2, - 1, -1):
            r[i] = prev * r[i + 1]
            prev = nums[i]

        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = l[i] * r[i]
        print(l)
        print(r)
        return res


nums = [-1, 1, 0, -3, 3]
# nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))
