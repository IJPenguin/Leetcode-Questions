class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        arr = s.split(" ")
        pat = [*pattern]
        if len(pat) != len(arr):
            return False

        for string, p in zip(arr, pat):
            print(d)
            if string in d and d[string] == p:
                continue
            elif string not in d:
                if p not in d.values():
                    d[string] = p
                    continue
            return False

        return True

pattern = "abba"
s = "dog cat cat dog"

# pattern = "abba"
# s = "dog cat cat fish"

# pattern = "aaaa"
# s = "dog cat cat dog"


pattern = "aaa"
s = "aa aa aa aa"

sol = Solution()
print(sol.wordPattern(pattern, s))
