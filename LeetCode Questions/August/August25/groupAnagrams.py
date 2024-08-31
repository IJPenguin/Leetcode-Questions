from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for string in strs:
            
            arr = [0] * 26

            for char in string:
                arr[ord(char) - ord('a')] += 1
            
            if d.get(tuple(arr)):
                d[tuple(arr)].append(string)
            else:
                d[tuple(arr)] = [string]

        return d.values()

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print(s.groupAnagrams(strs))