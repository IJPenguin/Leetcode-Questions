from typing import List
from collections import Counter

# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         res = 0
#         c = Counter(chars)

#         for word in words:
#             t = Counter(word)
#             a = True
#             for char, count in t.items():
#                 if char not in c or c[char] < count:
#                     a = False
#                     break
#             if not a:
#                 continue
#             res += len(word)
#         return res

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ### This is very efficient!!!! pay attention to the else place 
        count=0
        for i in words:
            for j in i:
                if i.count(j) > chars.count(j):
                    break
            else:  #### where to put this else is very very important!!!!! 
                count += len(i)
        return count
        

# words = ["cat","bt","hat","tree"]
# chars = "atach"       

words = ["hello", "world","leetcode"]
chars = "welldonehoneyr"

s = Solution()
print(s.countCharacters(words, chars))