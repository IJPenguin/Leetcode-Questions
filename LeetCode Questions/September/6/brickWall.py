from typing import List
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if len(wall) == 1:
            return 0
        
        val = sum(wall[0])
        if val == 1:
            return 0 
        
        

        
        pass

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
s = Solution()
print(s.leastBricks(wall))