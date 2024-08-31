from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        prev = [1]

        for i in range(rowIndex):

            t = [1]

            for j in range(1, i + 2):

                if j == i + 1:
                    t.append(1)
                else:
                    t.append(prev[j] + prev[j - 1])

            prev = t

        return prev


rowIndex =  6
s = Solution()
print(s.getRow(rowIndex))
