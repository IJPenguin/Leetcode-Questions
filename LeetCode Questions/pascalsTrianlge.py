from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1, numRows + 1):
            t = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    t.append(1)
                else: 
                    t.append(triangle[i - 2][j] + triangle[i - 2][j - 1])
            triangle.append(t)
        return triangle


numRows = 5
s = Solution()
print(s.generate(numRows))
