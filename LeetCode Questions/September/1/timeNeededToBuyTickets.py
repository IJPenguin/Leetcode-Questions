from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        val = tickets[k]
        for i, ticket in enumerate(tickets):
            if i <= k:
                if ticket > val:
                    ans += val
                else:
                    ans += ticket
            else:
                if ticket < val:
                    ans += ticket
                else:
                    ans += val - 1

        return ans

    

tickets = [2,3,2]
k = 2        
# tickets = [5,1,1,1]
# k = 0
# tickets = [84,49,5,24,70,77,87,8]
# k = 3
# tickets = [4, 3, 2, 3, 1, 4]
# k = 2
s = Solution()
print(s.timeRequiredToBuy(tickets, k))