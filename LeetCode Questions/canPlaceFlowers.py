from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        
        if len(flowerbed) - 2 <= n:
            return False
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        




# flowerbed = [0, 0, 1, 0, 1]
# n = 1
# flowerbed = [1, 0, 0, 0, 1, 0, 0]
# n = 2
flowerbed = [1, 0, 0, 0, 1]
n = 1
# flowerbed = [1]
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
