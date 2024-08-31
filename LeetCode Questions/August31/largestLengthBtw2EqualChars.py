class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        s = [*s]
        chars = {}

        for i, char in enumerate(s):
            if char not in chars:
                chars[char] = [i]
            else:
                chars[char].append(i)

        ans = -1
        updated = False
        for char in chars.values():
            if len(char) >= 2:
                ans = max(ans, (max(char) - min(char)))
                updated = True
        if not updated:
            return ans
        return ans - 1


s1 = "aa"
s2 = "abca"
s3 = "cbzxy"
s4 = "cabbac"
s = Solution()
print(s.maxLengthBetweenEqualCharacters(s1))
print(s.maxLengthBetweenEqualCharacters(s2))
print(s.maxLengthBetweenEqualCharacters(s3))
print(s.maxLengthBetweenEqualCharacters(s4))
