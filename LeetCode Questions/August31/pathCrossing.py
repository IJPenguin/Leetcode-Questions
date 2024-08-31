class Solution:
    def isPathCrossing(self, path: str) -> bool:

        seen = set()

        start = [0, 0]

        seen.add(tuple(start))

        for dir in path:

            if dir == "N":
                start[1] += 1

            elif dir == "S":
                start[1] -= 1

            elif dir == "E":
                start[0] += 1

            elif dir == "W":
                start[0] -= 1

            if tuple(start) in seen:
                return True

            seen.add(tuple(start))

        return False


path1 = "NES"
path2 = "NESWW"
s = Solution()
print(s.isPathCrossing(path1))
print(s.isPathCrossing(path2))
