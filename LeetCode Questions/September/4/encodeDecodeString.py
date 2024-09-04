from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "_" + s
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s) :
            if s[i].isdigit() and s[i + 1] == "_":
                t = ""
                for j in range(i + 2, int(i + int(s[i]) + 2)):
                    t += s[j]
                res.append(t)
                i += int(s[i]) + 2

        return res
    
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "_" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            num = ""
            while True:
                if s[i] == "_":
                    i += 1
                    break
                else:
                    num += s[i]
                    i += 1
            num = int(num)
            res.append(s[i: i + num])
            i += num
        return res 


input = ["neet", "code", "love", "you"]
s = Solution()
encoded = s.encode(input)
decoded = s.decode(encoded)
print(encoded)
print(decoded)
