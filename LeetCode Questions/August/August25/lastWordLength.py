class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        word = False
        for i in range(len(s) - 1, -1, -1):
            if word:
                if s[i] == " ":
                    return res
                else:
                    res += 1
            else:
                if s[i] != " ":
                    word = True
                    res += 1
                
        return res


string1 = "Hello World"
string2 = "luffy is still joyboy"
string3 = "   fly me   to   the moon  "

s = Solution()
print(s.lengthOfLastWord(string1))
print(s.lengthOfLastWord(string2))
print(s.lengthOfLastWord(string3))
