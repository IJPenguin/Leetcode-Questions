# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         text = [*text]
#         balloon = "balloon"
#         found = True
#         count = 0
#         while found:
#             for char in balloon:
#                 if char in text:
#                     text.remove(char)
#                 else:
#                     found = False
#                     break
#             if found:
#                 count += 1
#         return count

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = { ch: 0 for ch in "balloon" }
        for ch in text:
            if ch in "balloon":
                balloon[ch] += 1
        balloon["l"] //= 2
        balloon["o"] //= 2
        res = float("inf")
        for val in balloon.values():
            res = min(res, val)
        return res
        

text = "loonbalxballpoon"
text = "leetcode"
text = "nlaebolko"
s = Solution()
print(s.maxNumberOfBalloons(text))
