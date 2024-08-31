from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, char in enumerate(s):
            if cnt[char] == 1:
                return i
        return -1
