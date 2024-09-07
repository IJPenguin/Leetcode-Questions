from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy = prices[0]
        
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                max_profit = max(prices[i] - buy, max_profit)
        return max_profit

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
s = Solution()
print(s.maxProfit(prices))