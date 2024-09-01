from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = Counter(students)

        for sandwich in sandwiches:
            if s[sandwich] > 0:
                s[sandwich] -= 1
            else:
                return sum(s.values())
            
        return 0
            



students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
s = Solution()
print(s.countStudents(students, sandwiches))
