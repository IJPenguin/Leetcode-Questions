from typing import List

# arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
# arrays = [[1,4],[0,5]]
arrays = [[1,4,5],[0,2]]
# arrays = [[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]]


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins = []
        maxs = []

        for arr in arrays:
            mins.append(arr[0])
            maxs.append(arr[-1])

        mn = min(mins)
        mx = max(maxs)

        if mins.index(mn) == maxs.index(mx):
            # check if the next min is bigger or the max is smaller
            mins.remove(mn)
            maxs.remove(mx)
            d1 = abs(min(mins) - mx)
            d2 = abs(max(maxs) - mn)
            return max(d1, d2)

        return abs(mn - mx)


s = Solution()
print(s.maxDistance(arrays))
