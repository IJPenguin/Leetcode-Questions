from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                
        if n <= 0:
            return True
        return False


# flowerbed = [0, 0, 1, 0, 1]
# n = 1

flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2

flowerbed = [1]
n = 1

flowerbed = [1, 0, 0, 0, 1]
n = 2

s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
