from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        s = sum(wall[0])
        hash = {}
        for w in wall:
            start = 0
            for val in w:
                start += val
                if start != s:
                    if start in hash:
                        hash[start] += 1
                    else:
                        hash[start] = 1
        if hash.values():
            val = max(hash.values())
        else:
            return n
        return n - val


wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
wall = [[2], [2], [2]]
s = Solution()
print(s.leastBricks(wall))
