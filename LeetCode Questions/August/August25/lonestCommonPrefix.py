from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
        
#         for i in range(len(strs[0])):
#             c = strs[0][i]
#             for j in range(1, len(strs)):
#                 if strs[j][i] != c or i == len(strs[j]):
#                     return strs[0][0:i]
#         return strs[0]        

strs = ["flower","flow","flight"]
s = Solution()    
print(s.longestCommonPrefix(strs))
