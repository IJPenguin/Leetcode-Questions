from typing import List
from collections import Counter


# class Solution:
#     def makeEqual(self, words: List[str]) -> bool:
#         total = {}
#         n = len(words)
#         for word in words:
#             c = Counter(word)
#             for char, count in c.items():
#                 if char in total:
#                     total[char] += count
#                 else:
#                     total[char] = count

#         for count in total.values():
#             if count % n != 0:
#                 return False
#         return True

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        ans = "".join(words)
        s = set(ans)
        for char in s:
            if ans.count(char) % n != 0:
                return False
        return True


words1 = ["abc", "aabc", "bc"]
words2 = ["ab", "a"]
s = Solution()
print(s.makeEqual(words1))
print(s.makeEqual(words2))
