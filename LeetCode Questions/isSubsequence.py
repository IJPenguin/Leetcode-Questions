s = "acb"
t = "ahbgdc"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while j < len(s):
            if i >= len(t):
                return False
            if s[j] == t[i]:
                covered += s[j]
                j += 1
            i += 1
        return True


sol = Solution()
print(sol.isSubsequence(s, t))
