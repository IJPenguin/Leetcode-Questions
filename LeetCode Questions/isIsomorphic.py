class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            elif d[s[i]] == t[i]:
                continue
            else:
                return False

        return True


# s = "bbbaaaba"
# t = "aaabbbba"
s = "badc"
t = "baba"
sol = Solution()
print(sol.isIsomorphic(s, t))
